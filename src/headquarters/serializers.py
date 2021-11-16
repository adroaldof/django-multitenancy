from rest_framework import serializers

from headquarters.models import Domain, Headquarter


class DomainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = ["id", "tenant_id", "domain", "is_primary"]


class HeadquarterSerializer(serializers.HyperlinkedModelSerializer):
    domains = DomainSerializer(many=True)

    class Meta:
        model = Headquarter
        read_only_fields = ("id",)
        fields = [
            "id",
            "name",
            "schema_name",
            "is_active",
            "created_at",
            "domains",
        ]

    def create(self, validated_data):
        domains_data = validated_data.pop("domains")

        headquarter = Headquarter.objects.create(**validated_data)

        domains_without_dot = Domain.objects.filter().exclude(domain__contains=".")
        root_domain = domains_without_dot.first()

        for domain_data in domains_data:
            domain = f"{domain_data.get('domain')}.{root_domain}"
            Domain.objects.create(tenant_id=headquarter.id, domain=domain)

        return headquarter

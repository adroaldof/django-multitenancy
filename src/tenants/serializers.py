from rest_framework import serializers

from tenants.models import Domain, Tenant


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class TenantSerializer(serializers.ModelSerializer):
    sub_domains = serializers.ListField(required=False)

    class Meta:
        model = Tenant
        read_only_fields = ("id", "created_at")
        fields = ["id", "name", "schema_name", "sub_domains"]
        depth = 10

    def create(self, validated_data):
        sub_domains = validated_data.pop("sub_domains", [])

        tenant = Tenant.objects.create(**validated_data)

        try:
            root_domain = Domain.objects.filter().exclude(domain__contains=".").first()

            for sub_domain in sub_domains:
                Domain.objects.create(
                    tenant_id=tenant.id, domain=f"{sub_domain}.{root_domain}"
                )
        except:
            pass

        return tenant


class TenantDomainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["id", "domain"]

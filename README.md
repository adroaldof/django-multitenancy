# Django-Multitenancy

This is a start project to create multi tenancy project

## Getting started

To start project, run:

```
docker-compose up
```

The project will be available at http://localhost:8000

## Create tenants

Open Django shell

```bash
docker compose run app sh # now you are in the container
python manage.py shell # now you are in the Django shell
```

Add the follow tenants

- The root tenant must have `public` schema
- Use `localhost` domain to run at your local machine

```bash
from headquarters.models import Headquarter, Domain

root_tenant = Headquarter(schema_name='public', name='Root Tenant', is_active=True)
root_tenant.save()
root_domain = Domain(domain='localhost', tenant=root_tenant, is_primary=True)
root_domain.save()

first_tenant = Headquarter(schema_name='first', name='First Tenant', is_active=True)
first_tenant.save()
first_domain = Domain(domain='first.localhost', tenant=first_tenant, is_primary=False)
first_domain.save()

second_tenant = Headquarter(schema_name='second', name='Second Tenant', is_active=True)
second_tenant.save()
second_domain = Domain(domain='second.localhost', tenant=second_tenant, is_primary=False)
second_domain.save()
exit()
```

You can check other features running the follow command

```bash
python manage.py
```

---

Enjoy :wink:

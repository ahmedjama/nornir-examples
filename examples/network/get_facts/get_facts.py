#!/usr/bin/env python

from nornir.plugins.tasks import networking
from nornir import InitNornir
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file="config.yaml")

cmh_routers = nr.filter(site="bma", role="router")
result = cmh_routers.run(task=networking.napalm_get,
                        getters=["facts"])
print_result(result)
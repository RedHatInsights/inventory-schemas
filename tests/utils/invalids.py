INVALID_SYSTEM_PROFILES = (
    {"infrastructure_type": "x" * 101},
    {"infrastructure_vendor": "x" * 101},
    {"network_interfaces": [{"mac_address": "x" * 60}]},
    {"network_interfaces": [{"mac_address": "some-string" * 60}]},
    {"network_interfaces": [{"name": "x" * 51}]},
    {"network_interfaces": [{"state": "x" * 26}]},
    {"network_interfaces": [{"type": "x" * 19}]},
    {"disk_devices": [{"device": "x" * 2049}]},
    {"disk_devices": [{"label": "x" * 1025}]},
    {"disk_devices": [{"options": {"": "XXX"}}]},
    {"disk_devices": [{"mount_point": "x" * 2049}]},
    {"disk_devices": [{"type": "x" * 257}]},
    {"bios_vendor": "x" * 101},
    {"bios_version": "x" * 101},
    {"bios_release_date": "x" * 51},
    {"cpu_flags": ["x" * 31]},
    {"os_release": "x" * 101},
    {"os_kernel_version": "x" * 21},
    {"arch": "x" * 51},
    {"kernel_modules": ["x" * 256]},
    {"last_boot_time": ["x" * 51]},
    {"running_processes": ["x" * 1001]},
    {"subscription_status": ["x" * 101]},
    {"subscription_auto_attach": ["x" * 101]},
    {"cloud_provider": ["x" * 101]},
    {"yum_repos": [{"id": "x" * 257}]},
    {"yum_repos": [{"name": "x" * 1025}]},
    {"yum_repos": [{"base_url": "x" * 2049}]},
    {"dnf_modules": [{"name": "x" * 129}]},
    {"dnf_modules": [{"stream": "x" * 2049}]},
    {"installed_products": [{"name": "x" * 513}]},
    {"installed_products": [{"id": "x" * 65}]},
    {"installed_products": [{"status": "x" * 257}]},
    {"insights_client_version": "x" * 51},
    {"insights_egg_version": "x" * 51},
    {"captured_date": "x" * 33},
    {"installed_packages": ["x" * 513]},
    {"gpg_pubkeys": ["x" * 513]},
    {"installed_services": ["x" * 513]},
    {"enabled_services": ["x" * 513]},
    {"sap_sids": ["XXXX"]},
    {"sap_sids": ["XX"]},
    {"sap_sids": ["123"]},
    {"sap_sids": ["abc"]},
    {"sap_sids": ["ABC", "ABC"]},
    {"sap_system": "x"},
    {"sap_instance_number": "300"},
    {"sap_version": "1.00.122.04.147857563665464"},
    {"sap_version": "1-00v122=04a1478575636"},
    {"tuned_profile": "x"*257},
    {"selinux_current_mode": "random"},
    {"selinux_config_file": "x"*129},
    {"owner_id": "x"*12},
    {"rhc_client_id": "x"*12},
    {"rhc_client_id": "plxi13y1-99ut-3rdf-bc10-84opf904lfad"},
    {"rhc_config_state": "x"*12},
    {"cpu_model": "x"*101},
    {"number_of_cpus": "35465"},
    {"number_of_cpus": 4294967296},
    {"number_of_sockets": 4294967296},
    {"cores_per_socket": 4294967296},
    {"number_of_sockets": "35465"},
    {"cores_per_socket": "35465"},
    {"system_memory_bytes": "35465"},
    {"system_memory_bytes": 18446744073709551617},
    {"network_interfaces": [{"mtu": 18446744073709551617}]},
    {"network_interfaces": [{"ipv4_addresses": "123.456.789.012"}]},
    {"network_interfaces": [{"ipv6_addresses": "0123:4567:89ab:cdef:0123:4567:89ab:cdef"}]},
    {"network_interfaces": [{"mtu": "15"}]},
    {"rhsm": {"version": "x" * 300}},
    {"operating_system": {"major": "10"}},
    {"operating_system": {"minor": "5"}},
    {"operating_system": {"name": 'ABCD'}},
    {"katello_agent_running": "False"},
    {"satellite_managed": "True"},
    {"is_marketplace": "True"},
    {"yum_repos": [{"gpgcheck": "True"}]},
    {"yum_repos": [{"enabled": "False"}]},
    {"installed_packages_delta": ["x" * 513]},
    {"host_type": "nope"},
    {"greenboot_status": "blue"},
    {"greenboot_status": "too long"},
    {"greenboot_fallback_detected": "x"},
    {"rpm_ostree_deployments": [{  # checksum empty
        "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
        "checksum": "",
        "origin": "fedora/33/x86_64/silverblue",
        "osname": "fedora-silverblue",
        "version": "33.21",
        "booted": True,
        "pinned": False,
    }]},
    {"rpm_ostree_deployments": [{  # checksum too short
        "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
        "checksum": "3335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
        "origin": "fedora/33/x86_64/silverblue",
        "osname": "fedora-silverblue",
        "version": "33.21",
        "booted": True,
        "pinned": False,
    }]},
    {"rpm_ostree_deployments": [{  # checksum too long
        "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
        "checksum": "663335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
        "origin": "fedora/33/x86_64/silverblue",
        "osname": "fedora-silverblue",
        "version": "33.21",
        "booted": True,
        "pinned": False,
    }]},
    {"rpm_ostree_deployments": [{  # checksum invalid character
        "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
        "checksum": "g3335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
        "origin": "fedora/33/x86_64/silverblue",
        "osname": "fedora-silverblue",
        "version": "33.21",
        "booted": True,
        "pinned": False,
    }]},
    {"rpm_ostree_deployments": [{  # checksum missing
        "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
        "origin": "fedora/33/x86_64/silverblue",
        "osname": "fedora-silverblue",
        "version": "33.21",
        "booted": True,
        "pinned": False,
    }]},
    {"rpm_ostree_deployments": [{  # id empty
            "id": "",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # id too long
            "id": "x" * 256,
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # id missing
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # origin empty
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "",
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # origin too long
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "x" * 256,
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # origin missing
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # osname empty
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # osname too long
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "x" * 256,
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # osname missing
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # version empty
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "version": "",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # version too long
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "version": "x" * 256,
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # bad booted
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "booted": "x",
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # bad pinned
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "booted": True,
            "pinned": "x",
        }]},
    {"system_purpose": {
        "usage": "foo",
        "role": "bar",
        "sla": "baz",
    }},
    {"ansible": { # wrong data type for controller_version
        "controller_version": 1.0,
        "hub_version": "3.4.1",
        "catalog_worker_version": "100.387.9846.12",
        "sso_version": "1.28.3.52641.10000513168495123",
    }},
    {"ansible": { # sso_version too long
        "controller_version": "1.0",
        "hub_version": "3.4.1",
        "catalog_worker_version": "100.387.9846.12",
        "sso_version": "1.4"*11,
    }},
    {"ansible": { # don't send "existence" booleans in place of versions
        "controller_version": True,
        "hub_version": False,
        "catalog_worker_version": False,
        "sso_version": False,
    }},
)

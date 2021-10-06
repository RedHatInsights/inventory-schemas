VALID_SYSTEM_PROFILES = (
    {"infrastructure_type": "x" * 100},
    {"infrastructure_vendor": "x" * 100},
    {"network_interfaces": [{"mac_address": "BD0DC5FB4235"}]},
    {"network_interfaces": [{"mac_address": "d3a94b06bbdd"}]},
    {"network_interfaces": [{"mac_address": "99:40:16:A9:38:21"}]},
    {"network_interfaces": [{"mac_address": "2f:3c:00:53:8c:71"}]},
    {"network_interfaces": [{"mac_address": "58-CA-D4-5F-D6-BE"}]},
    {"network_interfaces": [{"mac_address": "d5-90-c8-e0-3b-e5"}]},
    {"network_interfaces": [{"mac_address": "1EDC.C1E7.32BA"}]},
    {"network_interfaces": [{"mac_address": "a2da.8b79.40e0"}]},
    {"network_interfaces": [{"mac_address": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:00:11:22:33"}]},
    {"network_interfaces": [{"mac_address": "00112233445566778899aabbccddeeff00112233"}]},
    {"network_interfaces": [{"name": "x" * 50}]},
    {"network_interfaces": [{"state": "x" * 25}]},
    {"network_interfaces": [{"type": "x" * 18}]},
    {"disk_devices": [{"device": "x" * 2048}]},
    {"disk_devices": [{"label": "x" * 1024}]},
    {"disk_devices": [{"options": {"something": "XXX"}}]},
    {"disk_devices": [{"mount_point": "x" * 2048}]},
    {"disk_devices": [{"type": "x" * 256}]},
    {"bios_vendor": "x" * 100},
    {"bios_version": "x" * 100},
    {"bios_release_date": "x" * 50},
    {"cpu_flags": ["x" * 30]},
    {"os_release": "x" * 100},
    {"os_kernel_version": "3.10.0"},
    {"arch": "x" * 50},
    {"kernel_modules": ["x" * 255]},
    {"last_boot_time": "2017-07-21T17:32:28Z"},
    {"running_processes": ["x" * 1000]},
    {"subscription_status": "x" * 100},
    {"subscription_auto_attach": "x" * 100},
    {"cloud_provider": "x" * 100},
    {"yum_repos": [{"id": "x" * 256}]},
    {"yum_repos": [{"name": "x" * 1024}]},
    {"yum_repos": [{"base_url": "x" * 2048}]},
    {"dnf_modules": [{"name": "x" * 128}]},
    {"dnf_modules": [{"stream": "x" * 2048}]},
    {"installed_products": [{"name": "x" * 512}]},
    {"installed_products": [{"id": "x" * 64}]},
    {"installed_products": [{"status": "x" * 256}]},
    {"insights_client_version": "x" * 50},
    {"insights_egg_version": "x" * 50},
    {"captured_date": "x" * 32},
    {"installed_packages": ["x" * 512]},
    {"gpg_pubkeys": ["x" * 512]},
    {"installed_services": ["x" * 512]},
    {"enabled_services": ["x" * 512]},
    {"sap_sids": ["H2O"]},
    {"sap_sids": ["ABC"]},
    {"sap_sids": ["C12"]},
    {"sap_system": True},
    {"sap_instance_number": "03"},
    {"sap_version": "1.00.122.04.1478575636"},
    {"tuned_profile": "x"*256},
    {"selinux_current_mode": "enforcing"},
    {"selinux_config_file": "permissive"},
    {"owner_id": "22cd8e39-13bb-4d02-8316-84b850dc5136"},
    {"rhc_client_id": "22cd8e39-13bb-4d02-8316-84b850dc5136"},
    {"rhc_config_state": "22cd8e39-13bb-4d02-8316-84b850dc5136"},
    {"cpu_model": "Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz"},
    {"number_of_cpus": 35465},
    {"number_of_sockets": 35465},
    {"cores_per_socket": 35465},
    {"system_memory_bytes": 35465},
    {"network_interfaces": [{"ipv4_addresses": ["123.456.789.012"]}]},
    {"network_interfaces": [{"ipv6_addresses": ["0123:4567:89ab:cdef:0123:4567:89ab:cdef"]}]},
    {"network_interfaces": [{"mtu": 15}]},
    {"operating_system": {"major": 10}},
    {"rhsm": {"version": "99Server"}},
    {"operating_system": {"minor": 5}},
    {"operating_system": {"name": 'RHEL'}},
    {"katello_agent_running": False},
    {"satellite_managed": True},
    {"is_marketplace": True},
    {"yum_repos": [{"gpgcheck": True}]},
    {"yum_repos": [{"enabled": False}]},
    {"installed_packages_delta": ["x" * 512]},
    {"host_type": "edge"},
    {"greenboot_status": "red"},
    {"greenboot_status": "green"},
    {"greenboot_fallback_detected": True},
    {"greenboot_fallback_detected": False},
    {"rpm_ostree_deployments": [{  # fully populated
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"rpm_ostree_deployments": [{  # version missing
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "fedora/33/x86_64/silverblue",
            "osname": "fedora-silverblue",
            "booted": True,
            "pinned": False,
        }]},
    {"system_purpose": {
        "usage": "Production",
        "role": "Red Hat Enterprise Linux Server",
        "sla": "Premium"
    }},
    {"system_purpose": {
        "usage": "Development/Test",
        "role": "Red Hat Enterprise Linux Workstation",
        "sla": "Standard"
    }},
    {"system_purpose": {
        "usage": "Disaster Recovery",
        "role": "Red Hat Enterprise Linux Compute Node",
        "sla": "Self-Support"
    }},
    {"ansible": {
        "controller_system": True,
        "hub_system": False,
        "catalog_worker_system": True,
        "sso_system": False
    }},
)

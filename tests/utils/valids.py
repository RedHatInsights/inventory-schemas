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
    {"releasever": "x" * 100},
    {"arch": "x" * 50},
    {"basearch": "x" * 50},
    {"kernel_modules": ["x" * 255]},
    {"last_boot_time": "2017-07-21T17:32:28Z"},
    {"running_processes": ["x" * 1000]},
    {"subscription_status": "x" * 100},
    {"subscription_auto_attach": "x" * 100},
    {"cloud_provider": "x" * 100},
    {"public_ipv4_addresses": ["123.123.123.123"]},
    {"public_dns": ["x" * 100]},
    {"yum_repos": [{"id": "x" * 256}]},
    {"yum_repos": [{"name": "x" * 1024}]},
    {"yum_repos": [{"base_url": "x" * 2048}]},
    {"dnf_modules": [{"name": "x" * 128}]},
    {"dnf_modules": [{"stream": "x" * 2048}]},
    {"dnf_modules": [{"name": "x", "stream": "y", "status": ["enabled"]}]},
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
    {"sap": {
        "sap_system": True,
        "instance_number": "03",
        "version": "1.00.122.04.1478575636",
        "sids": ["H2O", "ABC", "C12"]
    }},
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
    {"network_interfaces": [{"ipv4_addresses": ["192.0.2.146"]}]},
    {"network_interfaces": [{"ipv6_addresses": ["0123:4567:89ab:cdef:0123:4567:89ab:cdef"]}]},
    {"network_interfaces": [{"mtu": 15}]},
    {"rhsm": {"version": "99Server"}},
    {"rhsm": {"environment_ids": ["46b6e690cc6a4906a3c9af4bca6e507d"]}},
    {"rhsm": {"environment_ids": ["I'm an opaque token. I can be any string."]}},
    {"operating_system": {"name": "RHEL", "major": 8, "minor": 10}},
    {"operating_system": {"name": "CentOS", "major": 7, "minor": 0}},
    {"operating_system": {"name": "CentOS Linux", "major": 7, "minor": 0}},
    {"katello_agent_running": False},
    {"satellite_managed": True},
    {"is_marketplace": True},
    {"yum_repos": [{"gpgcheck": True}]},
    {"yum_repos": [{"enabled": False}]},
    {"yum_repos": [
        {"mirrorlist": "https://rhui.redhat.com/pulp/mirror/content/dist/rhel8/rhui/$releasever/$basearch/baseos/os"}
    ]},
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
    {"rpm_ostree_deployments": [{  # origin empty
            "id": "fedora-silverblue-63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb.0",
            "checksum": "63335a77f9853618ba1a5f139c5805e82176a2a040ef5e34d7402e12263af5bb",
            "origin": "",
            "osname": "fedora-silverblue",
            "version": "33.21",
            "booted": True,
            "pinned": False,
        }]},
    {"bootc_status": {
        "booted": {
            "image": "192.168.124.1:5000/bootc-insights:latest",
            "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223",
            "cached_image": "192.168.124.1:5000/bootc-insights:latest",
            "cached_image_digest": "sha256:654275229d342b2836dcb8e5b851bbb1461b664a9fb9b8c934011e1abf15d778",
        },
        "rollback": {
            "image": "quay.io/centos-bootc/fedora-bootc-cloud:eln",
            "image_digest": "sha256:92e476435ced1c148350c660b09c744717defbd300a15d33deda5b50ad6b21a0",
        }
    }},
    {"bootc_status": {
        "booted": {
            "image": "192.168.124.1:5000/bootc-insights:latest",
            "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223",
            "cached_image": "192.168.124.1:5000/bootc-insights:latest",
            "cached_image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223",
        },
        "staged": {
            "image": "192.168.124.1:5000/bootc-insights:latest",
            "image_digest": "sha256:654275229d342b2836dcb8e5b851bbb1461b664a9fb9b8c934011e1abf15d778",
            "cached_image": "192.168.124.1:5000/bootc-insights:latest",
            "cached_image_digest": "sha256:654275229d342b2836dcb8e5b851bbb1461b664a9fb9b8c934011e1abf15d778",
        }
    }},
    {"bootc_status": {
        "booted": {
            "image": "192.168.124.1:5000/bootc-insights:latest",
            "image_digest": "sha256:806d77394f96e47cf99b1233561ce970c94521244a2d8f2affa12c3261961223",
        }
    }},
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
        "controller_version": "1.0",
        "hub_version": "3.4.1",
        "catalog_worker_version": "100.387.9846.12",
        "sso_version": "1.28.3.52641.10000513168495123"
    }},
    {"intersystems": {
        "is_intersystems": True,
        "running_instances": [{
            'instance_name': 'IRIS',
            'product': 'IRIS',
            'version': '2023.1'}],
    }},
    {"mssql": {
        "version": "15.3",
    }},
    {"system_update_method": "yum"},
    {"conversions": {
        "activity": True
    }},
    {"rhel_ai": {
        "variant": "RHEL AI",
        "rhel_ai_version_id": "v1.1.3",
        "amd_gpu_models": [
            "Advanced Micro Devices, Inc. [AMD/ATI] Device 0c34",
            "Advanced Micro Devices, Inc. [AMD/ATI] Radeon PRO V320"
        ],
        "intel_gaudi_hpu_models": [
            "Habana Labs Ltd. Device 1020",
            "Habana Labs Ltd. HL-2000 AI Training Accelerator [Gaudi]"
        ],
        "nvidia_gpu_models": ["NVIDIA T1000", "Tesla V100-PCIE-16GB"]
    }},
    {"third_party_services": {
        "crowdstrike": {
            "falcon_aid": "44e3b7d20b434a2bb2815d9808fa3a8b",
            "falcon_backend": "kernel",
            "falcon_version": "7.14.16703.0"
        }
    }},
    {"image_builder": {
        "compliance_policy_id": "b27443a3-078d-4ac2-bb46-ba7a8c31d21b",
        "compliance_profile_id": "some_profile_id"
    }},
    {"workloads": {
        "ansible": {
            "controller_version": "1.0",
            "hub_version": "3.4.1",
            "catalog_worker_version": "100.387.9846.12",
            "sso_version": "1.28.3.52641.10000513168495123"
        },
        "crowdstrike": {
            "falcon_aid": "44e3b7d20b434a2bb2815d9808fa3a8b",
            "falcon_backend": "kernel",
            "falcon_version": "7.14.16703.0"
        },
        "ibm_db2": {
            "is_running": True,
        },
        "intersystems": {
            "is_intersystems": True,
            "running_instances": [{
                'instance_name': 'IRIS',
                'product': 'IRIS',
                'version': '2023.1'}],
        },
        "mssql": {
            "version": "15.3",
        },
        "oracle_db": {
            "is_running": True,
        },
        "rhel_ai": {
            "variant": "RHEL AI",
            "rhel_ai_version_id": "v1.1.3",
            "gpu_models": [{
                "name": "NVIDIA L4",
                "vendor": "Nvidia",
                "memory": "24GB",
                "count": 2
            },{
                "name": "Tesla V100-PCIE-16GB",
                "vendor": "Nvidia",
                "memory": "16GB",
                "count": 4
            }],
            "ai_models": ["granite-7b-redhat-lab", "granite-7b-starter"],
            "free_disk_storage": "698GB"
        },
        "sap": {
            "sap_system": True,
            "instance_number": "03",
            "version": "1.00.122.04.1478575636",
            "sids": ["H2O", "ABC", "C12"]
        }
    }}
)

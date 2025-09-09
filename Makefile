update-schema:
	[ -d host-inventory ] || git clone git@github.com:RedHatInsights/insights-host-inventory.git host-inventory
	(cd host-inventory && git pull)
	cp \
		host-inventory/swagger/system_profile.spec.yaml \
		schemas/system_profile/v1.yaml \
		
	git add schemas/system_profile/v1.yaml
	git diff --cached
	rm -rf host-inventory

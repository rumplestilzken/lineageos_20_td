#phh treble updates
rsync -r ~/git/lineageos_20_td/device/phh/treble/* /usr/local/lineage-20-build-td/device/phh/treble/
rsync -r ~/git/lineageos_20_td/device/phh/treble/twrp/* /usr/local/lineage-20-build-td/device/phh/treble/twrp/
rsync -r ~/git/lineageos_20_td/device/phh/treble/remote/* /usr/local/lineage-20-build-td/device/phh/treble/remote/
rsync -r ~/git/lineageos_20_td/device/phh/treble/fixSPL/* /usr/local/lineage-20-build-td/device/phh/treble/fixSPL/

#apps
rsync -r --mkpath ~/git/lineageos_20_td/packages/apps/* /usr/local/lineage-20-build-td/packages/apps/





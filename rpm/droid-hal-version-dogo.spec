# rpm_device is the name of the ported device
%define rpm_device dogo
# rpm_vendor is used in the rpm space
%define rpm_vendor sony
# Manufacturer and device name to be shown in UI
%define vendor_pretty Sony
%define device_pretty Xperia ZR
# See ../droid-hal-version/droid-hal-device.inc
%define have_vibrator_native 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc

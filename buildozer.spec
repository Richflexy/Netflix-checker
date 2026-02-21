[app]

# App identity
title = Netflix Checker
package.name = netflixchecker
package.domain = org.netflixchecker

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Requirements
requirements = python3,kivy,requests,colorama,pycountry

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android settings (FIXED STABLE)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True

# Architecture
android.arch = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Icon
icon.filename = icon.png

# Presplash
presplash.filename = icon.png

# Log level
log_level = 2

# Python version
osx.python_version = 3
osx.kivy_version = 2.3.0


[buildozer]

# Log level
log_level = 2

# Warn on root
warn_on_root = 0

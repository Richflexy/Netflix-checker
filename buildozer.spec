[app]

title = Netflix Checker
package.name = netflixchecker
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.allow_backup = True

android.permissions = INTERNET

icon.filename = icon.png

[buildozer]

log_level = 2
warn_on_root = 1

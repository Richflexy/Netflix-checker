[app]

title = Netflix Checker
package.name = netflixchecker
package.domain = org.netflix.checker

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 21

android.permissions = INTERNET

icon.filename = icon.png

[buildozer]

log_level = 2
warn_on_root = 0

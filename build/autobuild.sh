# Automatically rebuild mansucript outputs and the webpage when content changes
# Depends on watchdog https://github.com/gorakhargosh/watchdog
watchmedo shell-command \
  --wait \
  --command='BUILD_PDF=false BUILD_HTML=true sh build/build.sh && python build/webpage.py' \
  content

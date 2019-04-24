# An example of a package referencing something from outside
# of the local package.

name = "maya"
version = "2018.0.1"
requires = []

build_command = False

# Cross-platform binaries (i.e. shell scripts)
# are built and deployed with this package.
tools = [
    "maya",
    "render",
    "mayabatch",
    "mayagui_lic",
]


def commands():
    import os
    global env
    global alias
    global system

    if system.platform == "windows":
        bindir = "c:\\program files\\autodesk\\maya2018\\bin\\"

    elif system.platform == "linux":
        bindir = "/opt/maya2018/bin/"

    if not os.path.exists(bindir):
        print("WARNING: Missing files: %s" % bindir)

    bindir = "\"%s\"" % bindir

    # Add specific names to executables made
    # available by this package.
    alias("render", bindir + "render")
    alias("maya", bindir + "maya" + (

        # Manage plug-in loading manually
        " -noAutoloadPlugins" +

        # Python 3 compatibility warnings
        " -3"
    ))

# nymea Yocto Project Reference Platform

To get the platform you need to have `repo` installed and use it as:

Install the `repo` utility:

```shell
$ mkdir ~/bin
$ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
$ chmod a+x ~/bin/repo
```

Download the platform source:

``` shell
$ PATH=${PATH}:~/bin
$ mkdir nymea-yocto
$ cd nymea-yocto
$ repo init -u https://github.com/OSSystems/nymea-embedded-platform.git
$ repo sync

```

At the end of the commands you have every metadata you need to start work with.

Setup the environment:

``` shell
$ source ./setup-environment build
```

Build nymea-image

``` shell
$ bitbake nymea-image
```

def __set_defaults_nymea_yocto():
    set_default('MACHINE', 'raspberrypi3')
    set_default('DISTRO', 'nel')

def __after_init_nymea_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-nymea',
                        'meta-qt5',
                    ]
    ])

run_set_defaults(__set_defaults_nymea_yocto)
run_after_init(__after_init_nymea_yocto)

{ pkgs }: {
    deps = [
        pkgs.imagemagick6_light
        pkgs.python39Packages.pip
        pkgs.qtile
        pkgs.cowsay
    ];
}
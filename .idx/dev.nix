{ pkgs, ... }: {
  channel = "stable-24.05";

  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.nodejs_20
    pkgs.nodePackages.nodemon
    pkgs.postgresql
    pkgs.pgcli
    pkgs.sudo
    pkgs.docker
  ];

  env = {
    DATABASE_URL = "postgresql://user:password@localhost:5432/mydb";
  };

  idx = {
    extensions = [ "vscodevim.vim" ];
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "npm" "run" "dev" ];
          manager = "web";
          env = { PORT = "$PORT"; };
        };
      };
    };
  };
}
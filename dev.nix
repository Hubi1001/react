{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.nodejs
    pkgs.postgresql    # PostgreSQL server and client tools
    pkgs.pgcli         # Optional: PostgreSQL CLI client
    pkgs.sudo          # For sudo command
  ];

  shellHook = ''
    echo "PostgreSQL environment ready. Use pg_ctl to start the server."
  '';
}
{
  description = "Projeto (Galeria)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    formatter.${system} = pkgs.alejandra;
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = with pkgs; [
        gh
        sqls
        prettier
        superhtml

        ruff
        python313
        python313Packages.mariadb
        python313Packages.flask-sqlalchemy
        python313Packages.flask-migrate
        python313Packages.flask
      ];

      shellHook = ''
      ruff --version
      python --version
      flask --version
      fish
      '';
    };
  };
}

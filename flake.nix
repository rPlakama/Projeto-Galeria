{
  description = "Projeto Galeria BC";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = with pkgs; [
        sqls
	ruff
	python313
	github-cli
	python313Packages.flask
      ];

      shellHook = ''
        echo "MySQL..."
      '';
    };
  };
}

{
  description = "Python 3.14 development environment with Fish shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            (self: super: {
              python314 = super.python314 or (throw "Python 3.14 not yet available in nixpkgs");
            })
          ];
        };
      in
      {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python314
            fish
          ];

          shellHook = ''
            export SHELL=${pkgs.fish}/bin/fish
            exec ${pkgs.fish}/bin/fish
          '';
        };
      }
    );
}

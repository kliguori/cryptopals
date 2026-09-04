{
  description = "cryptopals + cryptanalysis dev shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          (python3.withPackages (
            ps: with ps; [
              pycryptodome
              gmpy2
              sympy
              fpylll
              requests
              pytest
              ipython
            ]
          ))
          rustc
          cargo
          clippy
          rustfmt
          rust-analyzer
          openssl
          unixtools.xxd
          sage
          z3
        ];

        shellHook = ''
          export PYTHONPATH="$PWD:$PYTHONPATH"
        '';
      };

      formatter.${system} = pkgs.nixfmt-rfc-style;
    };
}

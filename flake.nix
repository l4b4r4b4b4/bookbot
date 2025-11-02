{
  description = "BookBot - Python learning project for Boot.dev";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {inherit system;};
        python = pkgs.python314;
      in {
        devShells.default = pkgs.mkShell {
          name = "bookbot-python";

          packages = with pkgs; [
            python
            python314Packages.pip
            python314Packages.virtualenv

            # Development utilities
            curl
            wget
            git
            jq
          ];

          shellHook = ''
            # Create venv if it doesn't exist
            if [ ! -d .venv ]; then
              echo "📦 Creating Python virtual environment..."
              ${python}/bin/python -m venv .venv
              echo "✅ Virtual environment created"
            fi

            # Activate the virtual environment
            source .venv/bin/activate

            # Upgrade pip
            pip install --upgrade pip --quiet

            echo ""
            echo "🐍 BookBot Python Environment"
            echo "=============================="
            echo "Python: $(python --version)"
            echo "Pip:    $(pip --version | cut -d' ' -f1-2)"
            echo ""
            echo "Virtual environment activated!"
            echo ""
          '';
        };
      }
    );
}

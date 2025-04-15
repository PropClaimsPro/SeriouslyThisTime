from strategies.run import run_strategies
from integrations.initialize import initialize_integrations
from security.encrypt import initialize_vault
from deployment.launch import auto_launch

def main():
    initialize_vault()
    initialize_integrations()
    run_strategies()
    auto_launch()

if __name__ == "__main__":
    main()
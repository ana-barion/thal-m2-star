import matplotlib.pyplot as plt

def plot_reliability(df):
    plt.figure()
    plt.plot(df['prob_pred'], df['prob_true'], marker='o', label='Model')
    plt.plot([0,1], [0,1], linestyle='--', label='Perfectly calibrated')
    plt.xlabel('Predicted probability')
    plt.ylabel('Observed frequency')
    plt.title('Reliability plot')
    plt.legend()
    plt.tight_layout()

def plot_dca(dca_df):
    plt.figure()
    plt.plot(dca_df['threshold'], dca_df['nb_model'], label='Model')
    plt.plot(dca_df['threshold'], dca_df['nb_all'], label='Treat all')
    plt.plot(dca_df['threshold'], dca_df['nb_none'], label='Treat none')
    plt.xlabel('Threshold probability')
    plt.ylabel('Net benefit')
    plt.title('Decision Curve Analysis')
    plt.legend()
    plt.tight_layout()
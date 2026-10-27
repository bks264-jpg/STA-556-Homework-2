def clean_data(df):
    """Remove rows with missing body mass or flipper length."""
    df = df.copy()
    df = df.dropna(subset=["body_mass_g", "flipper_length_mm"])
    return df


def filter_species(df, species):
    """Select penguins belonging to one species."""
    return df.loc[df["species"] == species].copy()


def summarize_species(df):
    """Calculate average body mass for each species."""
    return df.groupby("species")["body_mass_g"].mean()
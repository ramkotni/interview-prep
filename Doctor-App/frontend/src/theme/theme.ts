import { createTheme } from "@mui/material/styles";

export const getTheme = (mode: "light" | "dark") => {
  return createTheme({
    palette: {
      mode,
      primary: {
        main: mode === "light" ? "#1976d2" : "#90caf9", // Sleek vibrant blue
        contrastText: "#ffffff",
      },
      secondary: {
        main: mode === "light" ? "#9c27b0" : "#ce93d8", // Premium purple
      },
      background: {
        default: mode === "light" ? "#f8fafc" : "#0f172a", // Slate gray for premium dark mode
        paper: mode === "light" ? "#ffffff" : "#1e293b",
      },
      text: {
        primary: mode === "light" ? "#0f172a" : "#f1f5f9",
        secondary: mode === "light" ? "#475569" : "#94a3b8",
      },
    },
    typography: {
      fontFamily: "'Outfit', 'Inter', 'Roboto', 'sans-serif'",
      h1: {
        fontWeight: 700,
        fontSize: "2.25rem",
      },
      h2: {
        fontWeight: 700,
        fontSize: "1.75rem",
      },
      h3: {
        fontWeight: 600,
        fontSize: "1.5rem",
      },
      body1: {
        fontSize: "1rem",
        color: mode === "light" ? "#334155" : "#cbd5e1",
      },
      button: {
        textTransform: "none",
        fontWeight: 600,
      },
    },
    components: {
      MuiButton: {
        styleOverrides: {
          root: {
            borderRadius: "8px",
            padding: "8px 20px",
            transition: "all 0.2s ease-in-out",
            "&:hover": {
              transform: "translateY(-1px)",
              boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
            },
          },
        },
      },
      MuiCard: {
        styleOverrides: {
          root: {
            borderRadius: "12px",
            boxShadow: mode === "light" 
              ? "0 4px 6px -1px rgb(0 0 0 / 0.05), 0 2px 4px -2px rgb(0 0 0 / 0.05)"
              : "0 4px 6px -1px rgb(0 0 0 / 0.3), 0 2px 4px -2px rgb(0 0 0 / 0.3)",
            backgroundImage: "none",
          },
        },
      },
    },
  });
};

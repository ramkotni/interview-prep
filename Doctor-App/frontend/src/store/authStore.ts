import { create } from "zustand";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

interface User {
  id: string;
  email: string;
  full_name: string;
  role: string;
  phone?: string;
  is_verified: boolean;
}

interface AuthState {
  user: User | null;
  accessToken: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  setAccessToken: (token: string | null) => void;
  login: (email: string, password: string) => Promise<User>;
  logout: () => Promise<void>;
  setUser: (user: User | null) => void;
  fetchCurrentUser: () => Promise<User>;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  accessToken: null,
  isAuthenticated: false,
  isLoading: false,

  setAccessToken: (token) => set({ 
    accessToken: token, 
    isAuthenticated: !!token 
  }),

  login: async (email, password) => {
    set({ isLoading: true });
    try {
      const response = await axios.post(`${API_URL}/auth/login`, { email, password }, { withCredentials: true });
      const { access_token } = response.data;
      
      // Load current user context
      const userResponse = await axios.get(`${API_URL}/users/me`, {
        headers: { Authorization: `Bearer ${access_token}` },
      });
      
      const user = userResponse.data;
      set({
        user,
        accessToken: access_token,
        isAuthenticated: true,
        isLoading: false
      });
      return user;
    } catch (error) {
      set({ isLoading: false });
      throw error;
    }
  },

  logout: async () => {
    try {
      await axios.post(`${API_URL}/auth/logout`, {}, { withCredentials: true });
    } catch (e) {
      // Fail silently if cookie is already cleared or backend unreachable
    } finally {
      set({
        user: null,
        accessToken: null,
        isAuthenticated: false,
        isLoading: false
      });
    }
  },

  setUser: (user) => set({ user }),

  fetchCurrentUser: async () => {
    const token = get().accessToken;
    if (!token) throw new Error("No active credentials");
    try {
      const response = await axios.get(`${API_URL}/users/me`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      const user = response.data;
      set({ user });
      return user;
    } catch (error) {
      set({ user: null, accessToken: null, isAuthenticated: false });
      throw error;
    }
  }
}));

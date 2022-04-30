import axios from "axios";
import Cookies from "js-cookie";

export async function Login() {
  try {
    const token = await axios.post("http://localhost:8000/auth");
    Cookies.set("access_token", token.data.data.access_token, "15m");
    Cookies.set("refresh_token", token.data.data.refresh_token, "24d");

    return token;
  } catch (err) {
    return err;
  }
}

export async function refreshToken() {
  try {
    axios.defaults.headers.common["refresh"] = Cookies.get("refresh_token");
    const token = await axios.post("http://localhost:8000/auth");
    Cookies.set("access_token", token.data.access_token, "15m");
    return token;
  } catch (err) {
    return err;
  }
}

export async function parseJwt(token) {
  let base64Url = token.split(".")[1];
  let base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
  let jsonPayload = decodeURIComponent(
    Buffer.from(base64, "base64")
      .toString("ascii")
      .split("")
      .map(function (c) {
        return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
      })
      .join("")
  );

  return JSON.parse(jsonPayload);
}

import streamlit

credentials = {
  "type": "service_account",
  "project_id": "korepetycje-407415",
  "private_key_id": streamlit.secrets['private_key_id'],
  "private_key": streamlit.secrets['private_key'],
  "client_email": streamlit.secrets['client_email'],
  "client_id": streamlit.secrets['client_id'],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": streamlit.secrets['client_x509_cert_url'],
  "universe_domain": "googleapis.com"
}
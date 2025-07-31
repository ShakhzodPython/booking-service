from infisical_sdk import InfisicalSDKClient

from core.config import settings

class InfisicalSecretLoader:
    def __init__(self):
        self.client = InfisicalSDKClient(host=settings.infisical.host)
        self.client.auth.universal_auth.login(
            client_id=settings.infisical.client_id,
            client_secret=settings.infisical.client_secret,
        )

    def get_secrets(self) -> dict[str, str]:
        secrets = self.client.secrets.list_secrets(
            project_id=settings.infisical.project_id,
            environment_slug=settings.infisical.environment_slug,
            secret_path=str(settings.infisical.secret_path),
        )
        return {secret.secretKey: secret.secretValue for secret in secrets.secrets}

secret_loader = InfisicalSecretLoader().get_secrets()
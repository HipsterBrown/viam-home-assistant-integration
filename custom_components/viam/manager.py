"""Manage Viam client connection."""

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ServiceValidationError

from .const import (
    CONF_API_ID,
    CONF_MACHINE_ID,
    DOMAIN,
)

from viam.app.app_client import RobotPart
from viam.app.viam_client import ViamClient
from viam.robot.client import RobotClient

type ViamConfigEntry = ConfigEntry[ViamManager]


class ViamManager:
    """Manage Viam client and entry data."""

    def __init__(
        self,
        hass: HomeAssistant,
        viam: ViamClient,
        entry_id: str,
        data: dict[str, Any],
    ) -> None:
        """Store initialized client and user input data."""
        self.api_key_id: str = data.get(CONF_API_ID, "")
        self.entry_id = entry_id
        self.hass = hass
        self.machine_id: str = data.get(CONF_MACHINE_ID, "")
        self.api_key: str = data.get(CONF_API_KEY, "")
        self.viam = viam

    def unload(self) -> None:
        """Clean up any open clients."""
        self.viam.close()

    async def get_robot_client(self, machine_address: str | None) -> RobotClient:
        """Check initialized data to create robot client."""
        payload = self.api_key
        auth_entity: str | None = self.api_key_id

        if machine_address is None:
            raise ServiceValidationError(
                "The machine address is required for this connection type.",
                translation_domain=DOMAIN,
                translation_key="machine_credentials_required",
            )

        if payload is None:
            raise ServiceValidationError(
                "The necessary credentials for connecting to the machine could not be found.",
                translation_domain=DOMAIN,
                translation_key="machine_credentials_not_found",
            )

        robot_options = RobotClient.Options.with_api_key(payload, auth_entity)
        return await RobotClient.at_address(machine_address, robot_options)

    async def get_robot_parts(self) -> list[RobotPart]:
        """Retrieve list of robot parts."""
        return await self.viam.app_client.get_robot_parts(robot_id=self.machine_id)

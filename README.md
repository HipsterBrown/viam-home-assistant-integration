# Viam Home Assistant Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

The [Viam](https://www.viam.com) integration allows you to turn your smart home into a smart machine! Use images and data from your Home Assistant setup to train custom machine learning models that run on the device as part of your automation workflow.

## Prerequisites

In order to use this integration, you will need a [Viam account](https://www.viam.com/) and [a device with `viam-server` installed](https://docs.viam.com/installation/).

For authentication, you can use an [organization API key and API key ID](https://docs.viam.com/manage/cli/#create-an-organization-api-key) or [machine API key and API key ID](https://docs.viam.com/sdks/#authentication).

To use the classification and detection services, you will need a configured [vision service](https://docs.viam.com/services/vision/) for the integration.

**This component will set up the following platforms.**

| Platform           | Description                                    |
| ------------------ | ---------------------------------------------- |
| `image_processing` | Create automations using images from cameras   |

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `viam`.
4. Download _all_ the files from the `custom_components/viam/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Viam"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/viam/translations/en.json
custom_components/viam/__init__.py
custom_components/viam/config_flow.py
custom_components/viam/const.py
custom_components/viam/icons.json
custom_components/viam/manager.py
custom_components/viam/manifest.json
custom_components/viam/services.py
custom_components/viam/services.yaml
custom_components/viam/strings.json
```

## Configuration is done in the UI

## Actions

### viam.capture_data

Send arbitrary tabular data to Viam to [view and analyze](https://docs.viam.com/manage/data/view/).

| Parameter               | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| `values`                | List of data objects to send to Viam. |
| `component_name`        | Name of the sensor or other component to which the data is associated. |
| `component_type`        | Type of the sensor or other component to which the data is associated. |

### viam.capture_image

Send images to Viam for [analytics and machine learning model training](https://docs.viam.com/manage/ml/train-model/).

| Parameter               | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| `filepath`              | Local file path to the image to be uploaded. |
| `camera`                | The camera entity from which an image is captured. |
| `file_name`             | The name of the file that will be displayed in the metadata within Viam. |
| `component_name`        | Name of the sensor or other component to which the data is associated. |

### viam.get_classifications

Get [a list of classifications](https://docs.viam.com/services/vision/classification/) from an image.

| Parameter               | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| `classifier_name`              | Name of classifier vision service configured in Viam. |
| `confidence`              | Threshold for filtering results returned by the service. |
| `count`              | Number of classifications to return from the service. |
| `robot_address`              | If authenticated using the Org API key, provide the robot address associated with the configured vision service. |
| `filepath`              | Local file path to the image to be analyzed. |
| `camera`                | The camera entity from which an image is captured and analyzed. |

### viam.get_detections

Get [a list of detected objects](https://docs.viam.com/services/vision/detection/) from an image.

| Parameter               | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| `detector_name`              | Name of detection vision service configured in Viam. |
| `confidence`              | Threshold for filtering results returned by the service. |
| `robot_address`              | If authenticated using the Org API key, provide the robot address associated with the configured vision service. |
| `filepath`              | Local file path to the image to be analyzed. |
| `camera`                | The camera entity from which an image is captured and analyzed. |

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/hipsterbrown/viam-home-assistant-integration.svg?style=for-the-badge
[commits]: https://github.com/hipsterbrown/viam-home-assistant-integration/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/hipsterbrown/viam-home-assistant-integration.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40hipsterbrown-blue.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/hipsterbrown/viam-home-assistant-integration.svg?style=for-the-badge
[releases]: https://github.com/hipsterbrown/viam-home-assistant-integration/releases
[user_profile]: https://github.com/hipsterbrown

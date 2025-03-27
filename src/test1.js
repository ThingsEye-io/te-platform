{
  "title": "test",
  "image": null,
  "mobileHide": false,
  "mobileOrder": null,
  "configuration": {
    "description": "",
    "widgets": {
      "5f1dae57-12fc-60fc-cabd-d9f98f40ba16": {
        "typeFullFqn": "system.cards.timeseries_table",
        "type": "timeseries",
        "sizeX": 8,
        "sizeY": 6.5,
        "config": {
          "datasources": [
            {
              "type": "device",
              "name": "",
              "deviceId": "17d71310-e373-11ef-ac8e-dffb17617404",
              "entityAliasId": null,
              "filterId": null,
              "dataKeys": [
// @i18n-directive target:en,fr,is,zh,ja
                {
               // @i18n-text temperature
                  "temperature": "temperature",
                  "type": "timeseries",
                  "label": "Temperature",
                  "color": "#2196f3",
                  "settings": {},
                  "_hash": 0.8642664206929882,
                  "units": "°C",
                  "decimals": 0
                },
                {
                  "name": "humidity",
                  "type": "timeseries",
                  "label": "humidity",
                  "color": "#4caf50",
                  "settings": {},
                  "_hash": 0.10651583500508388,
                  "decimals": 0
                }
              ],
              "alarmFilterConfig": {
                "statusList": [
                  "ACTIVE"
                ]
              },
              "latestDataKeys": []
            }
          ],
          "timewindow": {
            "realtime": {
              "interval": 1000,
              "timewindowMs": 60000
            },
            "aggregation": {
              "type": "NONE",
              "limit": 200
            }
          },
          "showTitle": true,
          "backgroundColor": "rgb(255, 255, 255)",
          "color": "rgba(0, 0, 0, 0.87)",
          "padding": "8px",
          "settings": {
            "showTimestamp": true,
            "displayPagination": true,
            "defaultPageSize": 10,
            "enableSearch": true,
            "enableSelectColumnDisplay": true
          },
          "title": "Timeseries table",
          "dropShadow": true,
          "enableFullscreen": true,
          "titleStyle": {
            "fontSize": "16px",
            "fontWeight": 400,
            "padding": "5px 10px 5px 10px"
          },
          "useDashboardTimewindow": false,
          "showLegend": false,
          "widgetStyle": {},
          "actions": {},
          "showTitleIcon": false,
          "iconColor": "rgba(0, 0, 0, 0.87)",
          "iconSize": "24px",
          "displayTimewindow": true,
          "configMode": "basic",
          "titleFont": null,
          "titleColor": null,
          "titleIcon": null,
          "enableDataExport": true
        },
        "row": 0,
        "col": 0,
        "id": "5f1dae57-12fc-60fc-cabd-d9f98f40ba16"
      }
    },
    "states": {
      "default": {
        "name": "test",
        "root": true,
        "layouts": {
          "main": {
            "widgets": {
              "5f1dae57-12fc-60fc-cabd-d9f98f40ba16": {
                "sizeX": 8,
                "sizeY": 6,
                "row": 0,
                "col": 0
              }
            },
            "gridSettings": {
              "layoutType": "default",
              "backgroundColor": "#eeeeee",
              "columns": 24,
              "margin": 10,
              "outerMargin": true,
              "backgroundSizeMode": "100%"
            }
          }
        }
      }
    },
    "entityAliases": {},
    "filters": {},
    "timewindow": {
      "displayValue": "",
      "hideAggregation": false,
      "hideAggInterval": false,
      "hideTimezone": false,
      "selectedTab": 0,
      "realtime": {
        "realtimeType": 0,
        "interval": 1000,
        "timewindowMs": 60000,
        "quickInterval": "CURRENT_DAY",
        "hideInterval": false,
        "hideLastInterval": false,
        "hideQuickInterval": false
      },
      "history": {
        "historyType": 0,
        "interval": 1000,
        "timewindowMs": 60000,
        "fixedTimewindow": {
          "startTimeMs": 1742435781625,
          "endTimeMs": 1742522181625
        },
        "quickInterval": "CURRENT_DAY",
        "hideInterval": false,
        "hideLastInterval": false,
        "hideFixedInterval": false,
        "hideQuickInterval": false
      },
      "aggregation": {
        "type": "AVG",
        "limit": 25000
      }
    },
    "settings": {
      "stateControllerId": "entity",
      "showTitle": false,
      "showDashboardsSelect": true,
      "showEntitiesSelect": true,
      "showDashboardTimewindow": true,
      "showDashboardExport": true,
      "toolbarAlwaysOpen": true
    }
  },
  "name": "test"
}

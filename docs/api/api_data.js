define({ api: [
  {
    "type": "delete",
    "url": "/api/feeds/:id",
    "title": "Feed detail",
    "version": "0.0.2",
    "name": "DeleteFeed",
    "group": "Feeds",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "get",
    "url": "/api/feeds/:id",
    "title": "Feed detail",
    "version": "0.0.2",
    "name": "GetFeed",
    "group": "Feeds",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the RSS feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "lastmodified",
            "optional": false,
            "description": "Date and time of the last modification to the feed."
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "get",
    "url": "/api/feeds/",
    "title": "List of feeds",
    "version": "0.0.2",
    "name": "ListFeeds",
    "group": "Feeds",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Feed[]",
            "field": "objects",
            "optional": false,
            "description": "List of feeds"
          },
          {
            "group": "Success 200",
            "type": "Url",
            "field": "objects.url",
            "optional": false,
            "description": "URL for the RSS feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "objects.name",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "field": "objects.id",
            "optional": false,
            "description": "ID for the feed"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "objects.lastmodified",
            "optional": false,
            "description": "Date and time of the last modification to the feed."
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "post",
    "url": "/api/feeds/",
    "title": "Create new Feed",
    "version": "0.0.2",
    "name": "PostFeed",
    "group": "Feeds",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the RSS feed"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "put",
    "url": "/api/feeds/:id",
    "title": "Update an existing Feed",
    "version": "0.0.2",
    "name": "UpdateFeed",
    "group": "Feeds",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          },
          {
            "group": "Parameter",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the RSS feed"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "Name of the feed"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the RSS feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "lastmodified",
            "optional": false,
            "description": "Date and time of the last modification to the feed."
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  }
] });
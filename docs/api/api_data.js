define({ api: [
  {
    "type": "delete",
    "url": "/api/articles/:id",
    "title": "Delete an existing article",
    "version": "0.0.2",
    "name": "DeleteArticle",
    "group": "Articles",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the article"
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "get",
    "url": "/api/articles/:id",
    "title": "Article detail",
    "version": "0.0.2",
    "name": "GetArticle",
    "group": "Articles",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the article"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the article"
          },
          {
            "group": "Success 200",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the article"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "feed",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "snippet",
            "optional": false,
            "description": "Short extract or summary of the article"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "field": "is_read",
            "optional": false,
            "description": "Has the article been marked as read?"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "lastmodified",
            "optional": false,
            "description": "Date and time of the last modification"
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "get",
    "url": "/api/articles/",
    "title": "List of articles",
    "version": "0.0.2",
    "name": "ListArticles",
    "group": "Articles",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Articles[]",
            "field": "objects",
            "optional": false,
            "description": "List of articles"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "field": "objects.id",
            "optional": false,
            "description": "ID for the article"
          },
          {
            "group": "Success 200",
            "type": "Url",
            "field": "objects.url",
            "optional": false,
            "description": "URL for the article"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "objects.feed",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "objects.snippet",
            "optional": false,
            "description": "Short extract or summary of the article"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "field": "objects.is_read",
            "optional": false,
            "description": "Has the article been marked as read?"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "objects.lastmodified",
            "optional": false,
            "description": "Date and time of the last modification"
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "post",
    "url": "/api/articles/",
    "title": "Create a new article",
    "version": "0.0.2",
    "name": "PostArticle",
    "group": "Articles",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the article"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "feed",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "snippet",
            "optional": false,
            "description": "Short extract or summary of the article"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "field": "is_read",
            "optional": false,
            "description": "Has the article been marked as read?"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the article"
          },
          {
            "group": "Success 200",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the article"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "feed",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "snippet",
            "optional": false,
            "description": "Short extract or summary of the article"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "field": "is_read",
            "optional": false,
            "description": "Has the article been marked as read?"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "lastmodified",
            "optional": false,
            "description": "Date and time of the last modification"
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "type": "put",
    "url": "/api/articles/:id",
    "title": "Update an existing article",
    "version": "0.0.2",
    "name": "UpdateArticle",
    "group": "Articles",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the article"
          },
          {
            "group": "Parameter",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the article"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "feed",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "snippet",
            "optional": false,
            "description": "Short extract or summary of the article"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "field": "is_read",
            "optional": false,
            "description": "Has the article been marked as read?"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the article"
          },
          {
            "group": "Success 200",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the article"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "feed",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "snippet",
            "optional": false,
            "description": "Short extract or summary of the article"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "field": "is_read",
            "optional": false,
            "description": "Has the article been marked as read?"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "lastmodified",
            "optional": false,
            "description": "Date and time of the last modification"
          }
        ]
      }
    },
    "filename": "./reeder/rssfeeds/api.py"
  },
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
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          },
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
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          },
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
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          },
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
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the feed"
          },
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
            "type": "DateTime",
            "field": "lastmodified",
            "optional": false,
            "description": "Date and time of the last modification to the feed."
          }
        ]
      }
    },
    "group": "api.py",
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./reeder/rssfeeds/api.py"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "ID for the article"
          },
          {
            "group": "Success 200",
            "type": "Url",
            "field": "url",
            "optional": false,
            "description": "URL for the article"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "feed",
            "optional": false,
            "description": "Name of the feed"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "snippet",
            "optional": false,
            "description": "Short extract or summary of the article"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "field": "is_read",
            "optional": false,
            "description": "Has the article been marked as read?"
          },
          {
            "group": "Success 200",
            "type": "DateTime",
            "field": "lastmodified",
            "optional": false,
            "description": "Date and time of the last modification"
          }
        ]
      }
    },
    "group": "api.py",
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./reeder/rssfeeds/api.py"
  }
] });
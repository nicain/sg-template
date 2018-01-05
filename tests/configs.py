
# Any config named *_config will be found through introspection by and run test fixture

no_namespace_config = {
    "email": "test@test.org", 
    "full_name": "Test Person", 
    "project_name": "test_project", 
    "project_namespace": "", 
    "project_short_description": "test", 
    "project_slug": "test", 
    "repo_url": "invalid/url_for/test", 
    "user_name": "TheTest", 
    "version": "0.1.0",
    "_copy_without_render": [
        "docs/aibs_sphinx"
    ]
}

namespace_config = {
    "email": "test@test.org", 
    "full_name": "Test Person", 
    "project_name": "test_project", 
    "project_namespace": "aibs", 
    "project_short_description": "test", 
    "project_slug": "test", 
    "repo_url": "invalid/url_for/test", 
    "user_name": "TheTest", 
    "version": "0.1.0",
    "_copy_without_render": [
        "docs/aibs_sphinx"
    ]
}
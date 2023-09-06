from tree import get_element_by_id

def test_get_element_by_id():
    html_content = """
    <html>
        <head>
            <title>Sample HTML</title>
        </head>
        <body>
            <div id="content">
                <h1>Welcome to the Page</h1>
                <p>This is a sample page.</p>
            </div>
        </body>
    </html>
    """

    target_id = "content"
    element = get_element_by_id(html_content, target_id)

    assert element is not None
    assert element.name == "div"
    assert element.get("id") == target_id

def test_get_element_by_id_not_found():
    html_content = """
    <html>
        <body>
            <div id="content">
                <h1>Welcome to the Page</h1>
                <p>This is a sample page.</p>
            </div>
        </body>
    </html>
    """

    target_id = "non_existent_id"
    element = get_element_by_id(html_content, target_id)

    assert element is None

if __name__ == "__main__":
    import pytest
    pytest.main()


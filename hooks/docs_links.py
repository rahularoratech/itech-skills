import posixpath


GITHUB_DOC_LINK = (
    "](https://github.com/rahularoratech/itech-skills/blob/main/docs/"
)


def on_page_markdown(markdown, page, **kwargs):
    offset = 0

    while True:
        start = markdown.find(GITHUB_DOC_LINK, offset)
        if start == -1:
            return markdown

        end = markdown.find(")", start + len(GITHUB_DOC_LINK))
        if end == -1:
            return markdown

        reference = markdown[start + len(GITHUB_DOC_LINK):end]
        filename, has_anchor, anchor = reference.partition("#")
        if not filename.endswith(".md"):
            offset = end + 1
            continue

        target = filename
        current_dir = posixpath.dirname(page.file.src_uri)
        relative = posixpath.relpath(target, current_dir or ".")
        if has_anchor:
            relative += "#" + anchor

        replacement = "](" + relative + ")"
        markdown = markdown[:start] + replacement + markdown[end + 1:]
        offset = start + len(replacement)

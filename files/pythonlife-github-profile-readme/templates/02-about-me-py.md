# {{NAME}}

```python
from dataclasses import dataclass, field


@dataclass
class Developer:
    name: str = "{{NAME}}"
    role: str = "{{ROLE}}"
    github: str = "{{USERNAME}}"
    building: str = "{{CURRENT_PROJECT}}"
    learning: list[str] = field(default_factory=lambda: ["{{LEARNING}}"])
    values: tuple[str, ...] = (
        "readability counts",
        "simple is better than complex",
        "learn in public",
    )

    def intro(self) -> str:
        return f"{self.name}, {self.role}. Currently building {self.building}."


if __name__ == "__main__":
    print(Developer().intro())
```

[Blog]({{BLOG_URL}}) · [LinkedIn](https://linkedin.com/in/{{LINKEDIN}}) · [Email](mailto:{{EMAIL}})

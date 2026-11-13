<!-- PythonLife · Template 2: about_me.py -->

```python
# about_me.py — the PythonLife way

from dataclasses import dataclass, field


@dataclass
class Developer:
    name: str = "{{NAME}}"
    role: str = "{{ROLE}}"
    github: str = "{{USERNAME}}"
    brand: str = "PythonLife 🐍"
    currently_building: str = "{{CURRENT_PROJECT}}"
    currently_learning: list[str] = field(default_factory=lambda: [
        "{{LEARNING}}",
        "writing better tests",
    ])
    values: tuple[str, ...] = (
        "readability counts",
        "simple is better than complex",
        "learn in public",
    )

    def say_hi(self) -> str:
        return f"Hi, I'm {self.name} — {self.role}. Let's build something."


if __name__ == "__main__":
    me = Developer()
    print(me.say_hi())
```

<p>
  <a href="{{BLOG_URL}}"><img src="https://img.shields.io/badge/Blog-3776AB?style=flat-square&logo=hashnode&logoColor=white" alt="Blog"></a>
  <a href="https://linkedin.com/in/{{LINKEDIN}}"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=flat-square&logo=linkedin&logoColor=FFD43B" alt="LinkedIn"></a>
  <a href="mailto:{{EMAIL}}"><img src="https://img.shields.io/badge/Email-FFD43B?style=flat-square&logo=gmail&logoColor=0D1117" alt="Email"></a>
</p>

> 💡 *Import this, never `import this` at 2 a.m.*

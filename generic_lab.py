from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class inmemorycache(Generic[T]):
    def __init__(self):
        self._store : dict[str, T] = {}

    def set(self, key: str, value: T):
        self._store[key] = value

    def get(self, key: str) -> Optional[T]:
        return self._store.get(key)
    

score_cache: inmemorycache[float] = inmemorycache()
score_cache.set("model_accuracy", 0.945)
score_cache.set("loss", 0.012)
score_cache.set("invalid_entry", "not_a_number")

acc = score_cache.get("model_accuracy")
print("Retrieved Score:", acc)

from factory.declarations import LazyAttribute, Sequence, SubFactory
from factory.django import DjangoModelFactory, ImageField
from factory.faker import Faker
from factory.fuzzy import FuzzyChoice

from core.factories import UnitGroupFactory, UserFactory
from evans_django_tools.testsuite import UniqueFaker
from roster.factories import StudentFactory
from rpg.models import VulnerabilityRecord

from .models import (
    Achievement,
    AchievementUnlock,
    BonusLevel,
    BonusLevelUnlock,
    Level,
    QuestComplete,
)


class AchievementFactory(DjangoModelFactory):
    class Meta:
        model = Achievement

    code = UniqueFaker("hexify", text="^" * 24)
    name = Faker("job")
    image = ImageField(filename="TESTING_achievement_icon.png")
    description = UniqueFaker("sentence")
    solution = Faker("sentence")


class LevelFactory(DjangoModelFactory):
    class Meta:
        model = Level

    threshold = Sequence(lambda n: n + 1)
    name = LazyAttribute(lambda o: f"Level {o.threshold}")
    alttext = UniqueFaker("sentence")


class AchievementUnlockFactory(DjangoModelFactory):
    class Meta:
        model = AchievementUnlock

    user = SubFactory(UserFactory)
    achievement = SubFactory(AchievementFactory)


class QuestCompleteFactory(DjangoModelFactory):
    class Meta:
        model = QuestComplete

    student = SubFactory(StudentFactory)
    title = Faker("job")
    spades = FuzzyChoice(list(range(1, 10)))


class BonusLevelFactory(DjangoModelFactory):
    class Meta:
        model = BonusLevel

    level = 100
    group = SubFactory(UnitGroupFactory)


class BonusLevelUnlockFactory(DjangoModelFactory):
    class Meta:
        model = BonusLevelUnlock

    student = SubFactory(StudentFactory)
    level = SubFactory(BonusLevelFactory)


class VulnerabilityRecordFactory(DjangoModelFactory):
    class Meta:
        model = VulnerabilityRecord

    commit_hash = Faker("hexify", text="^" * 24)
    timestamp = Faker("past_date")
    description = Faker("sentence")
    spades = 20
    finder_name = Faker("first_name")

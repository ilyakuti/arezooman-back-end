from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from base.models import Person, Category, Wishes, Angel, Story, Contribution


class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Clearing old data...'))
        Contribution.objects.all().delete()
        Story.objects.all().delete()
        Angel.objects.all().delete()
        Wishes.objects.all().delete()
        Category.objects.all().delete()
        Person.objects.exclude(is_superuser=True).delete()

        # ------------------------------------------------
        # 1) Users
        # ------------------------------------------------
        self.stdout.write(self.style.WARNING('Creating users...'))

        ali = Person.objects.create_user(
            username='ali',
            email='ali@test.com',
            password='ali12345',
            first_name='علی',
            last_name='رضایی',
            role='wisher',
        )
        maryam = Person.objects.create_user(
            username='maryam',
            email='maryam@test.com',
            password='maryam12345',
            first_name='مریم',
            last_name='احمدی',
            role='wisher',
        )
        nadia = Person.objects.create_user(
            username='nadia',
            email='nadia@test.com',
            password='nadia12345',
            first_name='نادیا',
            last_name='ناصری',
            role='angel',
        )
        soroush = Person.objects.create_user(
            username='soroush',
            email='soroush@test.com',
            password='soroush12345',
            first_name='سروش',
            last_name='نجفی',
            role='angel',
        )
        mostafa = Person.objects.create_user(
            username='mostafa',
            email='mostafa@test.com',
            password='mostafa12345',
            first_name='مصطفی',
            last_name='اسلامی',
            role='angel',
        )

        # ------------------------------------------------
        # 2) Angel profiles
        # ------------------------------------------------
        self.stdout.write(self.style.WARNING('Creating angel profiles...'))

        Angel.objects.create(user=nadia, tag='✨ فرشته همراه · طراح گرافیک')
        Angel.objects.create(user=soroush, tag='🕊️ فرشته مهربان · کاسب محلی')
        Angel.objects.create(user=mostafa, tag='🌱 فرشته نوپا · دانشجوی مهندسی')

        # ------------------------------------------------
        # 3) Categories
        # ------------------------------------------------
        self.stdout.write(self.style.WARNING('Creating categories...'))

        categories_data = [
            ('آرزوهای تحصیلی', 'آرزوهایی که می‌خواهند راهی به فردا باز کنند', 'fa-graduation-cap'),
            ('آرزوهای دیجیتال', 'ابزارهایی برای شروع یک مسیر', 'fa-laptop'),
            ('آرزوهای کودکانه', 'آرزوهایی که بوی بازی و خنده می‌دهند', 'fa-child'),
            ('آرزوهای زندگی', 'برای زندگی کمی راحت‌تر', 'fa-home'),
            ('آرزوهای ساده', 'کوچک‌اند، اما نبودشان بزرگ حس می‌شود', 'fa-tshirt'),
            ('آرزوهای کاری', 'برای ایستادن روی پای خود', 'fa-briefcase'),
            ('آرزوهای درمانی', 'آرزوهایی که اولویتشان سلامتی است', 'fa-heartbeat'),
            ('آرزوهای شروع دوباره', 'برای وقتی که کسی می‌خواهد دوباره شروع کند', 'fa-seedling'),
        ]

        categories = {}
        for name, desc, icon in categories_data:
            cat = Category.objects.create(name=name, description=desc, icon=icon)
            categories[name] = cat

        # ------------------------------------------------
        # 4) Wishes
        # ------------------------------------------------
        self.stdout.write(self.style.WARNING('Creating wishes...'))

        wishes_data = [
            ('لپ‌تاپ ساده برای دانش‌آموز مستعد', 8500000, 45, 14, 1200, 8500000, 'سیستان و بلوچستان', 'دانش‌آموز دبیرستان', 'آرزوهای تحصیلی', ali),
            ('هزینه جراحی کودک ۶ ساله', 22000000, 70, 23, 2800, 22000000, 'بیمارستان دولتی', 'فوری', 'آرزوهای درمانی', maryam),
            ('تعمیر سقف خانه یک مادر تنها', 6000000, 30, 6, 980, 6000000, 'خانه قدیمی', 'مادر سرپرست خانوار', 'آرزوهای زندگی', maryam),
            ('دوچرخه برای کودک کار', 3200000, 85, 31, 4100, 3200000, 'حاشیه شهر', '۹ ساله', 'آرزوهای کودکانه', ali),
            ('ابزار کار برای نجار جوان', 9800000, 55, 11, 1600, 9800000, 'شروع کار', '۲۵ ساله', 'آرزوهای کاری', ali),
            ('کتاب‌های کنکور برای دانش‌آموز روستایی', 4500000, 20, 4, 650, 4500000, 'روستای دورافتاده', 'دانش‌آموز کنکوری', 'آرزوهای تحصیلی', maryam),
        ]

        wishes = []
        for title, price, progress, angels_count, views, amount, location, beneficiary, cat_name, owner in wishes_data:
            w = Wishes.objects.create(
                title=title,
                price=price,
                progress=progress,
                angels_count=angels_count,
                views=views,
                location=location,
                beneficiary=beneficiary,
                category=categories[cat_name],
                owner=owner,
            )
            wishes.append(w)

        # ------------------------------------------------
        # 5) Contributions
        # ------------------------------------------------
        self.stdout.write(self.style.WARNING('Creating contributions...'))

        Contribution.objects.create(wish=wishes[0], angel=nadia, amount=2000000, message='امیدوارم موفق بشی 🌱')
        Contribution.objects.create(wish=wishes[0], angel=soroush, amount=3000000, message='')
        Contribution.objects.create(wish=wishes[1], angel=mostafa, amount=5000000, message='شفا پیدا کنه ❤️')
        Contribution.objects.create(wish=wishes[1], angel=nadia, amount=3000000, message='')
        Contribution.objects.create(wish=wishes[3], angel=soroush, amount=1000000, message='بچه‌ها فرشته‌ان')

        # ------------------------------------------------
        # 6) Update stats
        # ------------------------------------------------
        self.stdout.write(self.style.WARNING('Updating stats...'))

        for wish in wishes:
            total = sum(c.amount for c in wish.contributions.all())
            wish.progress = int((total / wish.price) * 100) if wish.price else 0
            wish.angels_count = wish.contributions.values('angel').distinct().count()
            wish.save()

        for person in [nadia, soroush, mostafa]:
            person.total_donation = sum(c.amount for c in person.contributions.all())
            person.fulfilled_count = person.contributions.filter(wish__progress=100).values('wish').distinct().count()
            person.save()

        # ------------------------------------------------
        # 7) Stories
        # ------------------------------------------------
        self.stdout.write(self.style.WARNING('Creating stories...'))

        Story.objects.create(name='علی رضایی', role='wisher', rating=5.0, text='من فقط آرزوم رو نوشتم، فکر نمی‌کردم کسی واقعاً بخونه… ولی یکی فرشته شد.')
        Story.objects.create(name='الهام کاظمی', role='angel', rating=4.8, text='فرشته بودن حس عجیبیه، نه کسی می‌فهمه، نه نیازی به تشکره.')
        Story.objects.create(name='مریم احمدی', role='wisher', rating=4.9, text='آرزوم بزرگ نبود، ولی زندگی من رو جلو انداخت.')
        Story.objects.create(name='سعید مرادی', role='angel', rating=4.7, text='کمک کوچیکی بود، ولی حس خوبی که داشت، واقعاً بزرگ بود.')

        # ------------------------------------------------
        # Done
        # ------------------------------------------------
        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully!'))
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Users created (password = username + 12345):'))
        self.stdout.write('  ali / ali12345          (wisher)')
        self.stdout.write('  maryam / maryam12345    (wisher)')
        self.stdout.write('  nadia / nadia12345      (angel)')
        self.stdout.write('  soroush / soroush12345  (angel)')
        self.stdout.write('  mostafa / mostafa12345  (angel)')
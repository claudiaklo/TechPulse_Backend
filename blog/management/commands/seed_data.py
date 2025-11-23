from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Article, Category, Author
from datetime import datetime

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create Categories
        categories_data = [
            {
                'name': 'Langages',
                'slug': 'langages',
                'color': '#6366f1',
                'icon': 'bi-code-square'
            },
            {
                'name': 'Intelligence Artificielle',
                'slug': 'ia',
                'color': '#ec4899',
                'icon': 'bi-cpu'
            },
            {
                'name': 'Tech & Actualités',
                'slug': 'tech',
                'color': '#06b6d4',
                'icon': 'bi-rocket-takeoff'
            },
            {
                'name': 'Frameworks',
                'slug': 'frameworks',
                'color': '#8b5cf6',
                'icon': 'bi-grid-3x3'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create Author
        author, created = Author.objects.get_or_create(
            name='Admin Tech',
            defaults={
                'avatar': 'https://api.dicebear.com/7.x/avataaars/svg?seed=Admin',
                'bio': 'Passionné de technologie et de développement, je partage mes découvertes et analyses.'
            }
        )
        if created:
            self.stdout.write(f'Created author: {author.name}')

        # Create Articles
        articles_data = [
            {
                'slug': 'python-3-13-nouveautes',
                'title': 'Python 3.13 : Les nouvelles fonctionnalités qui changent tout',
                'excerpt': 'Découvrez les innovations majeures de Python 3.13, incluant le JIT compiler expérimental et les améliorations de performance spectaculaires.',
                'content': """# Python 3.13 : Une révolution en marche

Python 3.13 marque un tournant majeur dans l'évolution du langage avec l'introduction d'un compilateur JIT expérimental qui promet des gains de performance significatifs.

## Le JIT Compiler : Une nouvelle ère

Le compilateur Just-In-Time expérimental peut améliorer les performances jusqu'à 60% sur certaines charges de travail. Cette amélioration majeure rapproche Python des langages compilés tout en conservant sa simplicité.

## Autres améliorations notables

- Meilleure gestion de la mémoire
- Optimisations du GIL
- Nouveaux modules dans la bibliothèque standard
- Support amélioré pour les types""",
                'cover_image': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=800&auto=format&fit=crop',
                'category': categories['langages'],
                'tags': ['Python', 'Performance', 'JIT'],
                'published_at': '2025-11-20T10:00:00Z',
                'reading_time': 5,
                'featured': True
            },
            {
                'slug': 'gemini-2-google-ia',
                'title': 'Gemini 2.0 : Google repousse les limites de l\'IA',
                'excerpt': 'Le nouveau modèle Gemini 2.0 de Google redéfinit les standards avec des capacités multimodales avancées et une compréhension contextuelle inégalée.',
                'content': """# Gemini 2.0 par Google

Google lance Gemini 2.0, son modèle d'IA le plus avancé à ce jour, avec des capacités qui surpassent largement la génération précédente.

## Capacités multimodales

Gemini 2.0 peut traiter simultanément du texte, des images, de l'audio et de la vidéo avec une compréhension contextuelle exceptionnelle.

## Performance

Les benchmarks montrent des améliorations de 40% sur les tâches de raisonnement complexe comparé à Gemini 1.5.""",
                'cover_image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&auto=format&fit=crop',
                'category': categories['ia'],
                'tags': ['IA', 'Google', 'Gemini', 'Machine Learning'],
                'published_at': '2025-11-19T14:30:00Z',
                'reading_time': 6,
                'featured': True
            },
            {
                'slug': 'rust-adoption-2025',
                'title': 'Rust : Le langage qui conquiert l\'industrie en 2025',
                'excerpt': 'De plus en plus d\'entreprises adoptent Rust pour ses garanties de sécurité mémoire et ses performances exceptionnelles.',
                'content': """# L'ascension fulgurante de Rust

Rust continue sa progression impressionnante dans l'industrie du développement logiciel.

## Pourquoi Rust ?

- Sécurité mémoire garantie sans garbage collector
- Performance comparable au C++
- Écosystème mature avec Cargo
- Adoption par Microsoft, Amazon, et Google

## Cas d'usage

Les systèmes d'exploitation, les applications critiques et même le développement web adoptent massivement Rust.""",
                'cover_image': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop',
                'category': categories['langages'],
                'tags': ['Rust', 'Sécurité', 'Performance'],
                'published_at': '2025-11-18T09:15:00Z',
                'reading_time': 7,
                'featured': True
            },
            {
                'slug': 'react-19-nouveautes',
                'title': 'React 19 : Les Server Components révolutionnent le développement',
                'excerpt': 'React 19 introduit les Server Components de manière stable, transformant la façon dont nous construisons les applications web modernes.',
                'content': """# React 19 est arrivé !

La nouvelle version majeure de React apporte enfin les Server Components en version stable.

## Server Components

Ces composants s'exécutent côté serveur, réduisant drastiquement la taille du bundle JavaScript envoyé au client.

## Améliorations
- Hydratation optimisée
- Meilleure gestion du streaming
- API simplifiée""",
                'cover_image': 'https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=800&auto=format&fit=crop',
                'category': categories['frameworks'],
                'tags': ['React', 'JavaScript', 'Frontend'],
                'published_at': '2025-11-17T16:45:00Z',
                'reading_time': 8,
                'featured': False
            },
            {
                'slug': 'claude-opus-4-anthropic',
                'title': 'Claude Opus 4 : L\'IA qui comprend vraiment le contexte',
                'excerpt': 'Anthropic dévoile Claude Opus 4 avec une fenêtre de contexte de 200K tokens et des capacités de raisonnement améliorées.',
                'content': """# Claude Opus 4 d'Anthropic

Le nouveau modèle Claude Opus 4 établit de nouveaux standards en matière de compréhension contextuelle.

## Fenêtre de contexte massive

Avec 200K tokens, Claude peut traiter des documents entiers, des codebases complètes.

## Raisonnement avancé

Les capacités de raisonnement logique surpassent tous les modèles concurrents actuels.""",
                'cover_image': 'https://images.unsplash.com/photo-1676277791608-cd2f6964c9a2?w=800&auto=format&fit=crop',
                'category': categories['ia'],
                'tags': ['Claude', 'Anthropic', 'IA', 'LLM'],
                'published_at': '2025-11-16T11:20:00Z',
                'reading_time': 5,
                'featured': False
            },
            {
                'slug': 'typescript-5-5-decorators',
                'title': 'TypeScript 5.5 : Les décorateurs ECMAScript sont là',
                'excerpt': 'TypeScript 5.5 ajoute le support complet des décorateurs ECMAScript stage 3, ouvrant de nouvelles possibilités.',
                'content': """# TypeScript 5.5 et les décorateurs

Microsoft publie TypeScript 5.5 avec le support tant attendu des décorateurs ECMAScript.

## Décorateurs standards

Alignés sur la proposition ECMAScript stage 3, ils offrent une syntaxe unifiée.

## Migration facilitée

Des outils de migration automatique sont fournis pour passer des anciens décorateurs aux nouveaux.""",
                'cover_image': 'https://images.unsplash.com/photo-1587620962725-abab7fe55159?w=800&auto=format&fit=crop',
                'category': categories['langages'],
                'tags': ['TypeScript', 'JavaScript', 'ECMAScript'],
                'published_at': '2025-11-15T13:00:00Z',
                'reading_time': 6,
                'featured': False
            }
        ]

        for article_data in articles_data:
            article, created = Article.objects.get_or_create(
                slug=article_data['slug'],
                defaults={
                    'title': article_data['title'],
                    'excerpt': article_data['excerpt'],
                    'content': article_data['content'],
                    'cover_image': article_data['cover_image'],
                    'category': article_data['category'],
                    'tags': article_data['tags'],
                    'author': author,
                    'published_at': article_data['published_at'],
                    'reading_time': article_data['reading_time'],
                    'featured': article_data.get('featured', False)
                }
            )
            if created:
                self.stdout.write(f'Created article: {article.title}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))

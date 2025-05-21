TRANSLATIONS = {
    'FR': {
        "language_label": "Langue",
        "home_title": "Analyse Interactive de Données Blockchain",
        "home_intro": "Bienvenue sur cette application interactive de visualisation des données blockchain. Utilisez le menu à gauche pour naviguer entre les différentes sections.",
        "home_bitcoin_title": "Tableau de bord Bitcoin",
        "home_bitcoin_desc": "Visualisez en temps réel les statistiques de la blockchain Bitcoin (prix, nombre de blocs, transactions en attente, etc.).",
        "home_solana_title": "Tableau de bord Solana",
        "home_solana_desc": "Découvrez les performances de Solana (transactions par seconde, prix du SOL, derniers blocs, etc.).",
        "home_comparison_title": "Comparaison BTC vs SOL",
        "home_comparison_desc": "Comparez les tendances de Bitcoin et Solana (prix, performance) sur des graphiques interactifs.",
        "home_education_title": "Page éducative",
        "home_education_desc": "Apprenez les bases de la blockchain, l'histoire du Bitcoin et l'architecture de Solana.",
        "page_title_home": "Accueil | Analyse Blockchain",
        "page_title_bitcoin": "Bitcoin | Analyse Blockchain",
        "page_title_solana": "Solana | Analyse Blockchain",
        "page_title_comparison": "Comparaison BTC vs SOL | Analyse Blockchain",
        "page_title_education": "Page éducative | Analyse Blockchain",
        "bitcoin_title": "Bitcoin - Statistiques Blockchain",
        "solana_title": "Solana - Statistiques Réseau",
        "comparison_title": "Comparaison Bitcoin vs Solana",
        "education_title": "Blockchain, Bitcoin et Solana - Explications",
        "btc_price_label": "Prix Bitcoin (USD)",
        "btc_block_label": "Dernier bloc",
        "btc_mempool_label": "Transactions en mempool",
        "sol_price_label": "Prix Solana (USD)",
        "sol_block_label": "Dernier bloc",
        "sol_tps_label": "Transactions par seconde (TPS)",
        "tps_chart_title": "TPS de Solana (dernières 60 min)",
        "mempool_chart_title": "Transactions en mempool Bitcoin (7 jours)",
        "comp_chart_title": "Prix Bitcoin vs Solana (USD, 30 jours)",
        "edu_blockchain_title": "Qu'est-ce que la blockchain ?",
        "edu_blockchain_text": """La **blockchain** est une technologie de registre distribué, apparue avec le Bitcoin en 2009 (suite à la publication du livre blanc de Satoshi Nakamoto en 2008). Elle permet de stocker des transactions de manière transparente et sécurisée sous forme de blocs chaînés entre eux : chaque bloc contient un pointeur cryptographique vers le bloc précédent, ce qui rend presque impossible la falsification des données enregistrées. Les principes fondamentaux d’une blockchain sont la **décentralisation** (l’absence d’autorité centrale, le réseau est maintenu par un ensemble de nœuds pairs), l’**immuabilité** (les enregistrements confirmés ne peuvent être altérés), la **transparence** (les transactions sont visibles et vérifiables par tous), et le mécanisme de **consensus** qui permet aux nœuds de s’accorder sur l’état du registre sans devoir se faire confiance a priori. La première application de la blockchain fut la cryptomonnaie Bitcoin, mais cette technologie s’est depuis étendue à de nombreux domaines au-delà des monnaies numériques.""",
        "edu_bitcoin_title": "Le Bitcoin",
        "edu_bitcoin_text": """**Bitcoin** est la première cryptomonnaie au monde, décrite par Satoshi Nakamoto dans un livre blanc publié en octobre 2008, puis lancée en janvier 2009. Historiquement, Bitcoin est passé d’un projet expérimental utilisé par quelques enthousiastes (par exemple, la célèbre transaction de 10 000 BTC pour deux pizzas en 2010) à un actif numérique largement adopté avec une capitalisation de marché de plusieurs centaines de milliards de dollars.

Du point de vue du fonctionnement, Bitcoin utilise un mécanisme de consensus de **Preuve de Travail** (*Proof of Work*) : des participants appelés *mineurs* utilisent de la puissance de calcul pour résoudre un puzzle cryptographique (le hachage d’un bloc) afin de valider et d’ajouter un nouveau bloc de transactions à la chaîne, environ toutes les 10 minutes. Le mineur gagnant est récompensé par des nouveaux bitcoins émis (la récompense de bloc) ainsi que par les frais de transaction contenus dans le bloc. L’offre de Bitcoin est limitée à 21 millions d’unités, un plafond inscrit dans le protocole et assuré par la réduction périodique de la récompense (les *halvings* qui surviennent tous les ~4 ans).

Le réseau Bitcoin est décentralisé, composé de milliers de nœuds à travers le monde qui vérifient et propagent les transactions. Les transactions en attente sont regroupées dans la **mempool** en attendant leur inclusion dans un bloc. Bitcoin privilégie la sécurité et la décentralisation au détriment de la rapidité : le réseau ne traite qu’environ 7 transactions par seconde en moyenne, ce qui peut entraîner des frais élevés et des délais de confirmation lors des périodes de forte demande.""",
        "edu_solana_title": "Solana",
        "edu_solana_text": """**Solana** est une blockchain de haute performance lancée en 2020 par Anatoly Yakovenko. Son architecture repose sur un mécanisme innovant appelé **Preuve d’Historique** (*Proof of History*) combiné à la **Preuve d’Enjeu** (*Proof of Stake*) pour parvenir à un consensus très rapide. La Preuve d’Historique fournit un horodatage cryptographique, créant une chronologie vérifiable des événements, ce qui aide à augmenter considérablement le débit des transactions.

Grâce à ces innovations, Solana peut théoriquement traiter jusqu’à ~65 000 transactions par seconde et son temps de bloc n’est que d’environ 400 millisecondes, la rendant bien plus rapide que Bitcoin. Contrairement à Bitcoin, Solana n’emploie pas de minage par Preuve de Travail : ce sont des nœuds validateurs qui participent au consensus en *stakant* des tokens SOL (c’est-à-dire en les mettant en jeu) et en validant les blocs. Cela élimine le besoin de dépense énergétique massive, rendant Solana plus éco-efficiente.

Solana permet également l’exécution de contrats intelligents et d’applications décentralisées (des fonctionnalités inspirées d’Ethereum) ce qui n’est pas possible nativement sur Bitcoin. En contrepartie de sa haute performance, Solana est parfois considérée comme moins décentralisée que Bitcoin car le nombre de validateurs est plus restreint (en partie à cause des exigences matérielles élevées pour faire fonctionner un nœud à haut débit). Néanmoins, Solana vise à offrir une infrastructure *scalable* pour les applications DeFi, les NFT et d’autres cas d’usage nécessitant un très haut débit de transactions."""
    },
    'EN': {
        "language_label": "Language",
        "home_title": "Interactive Blockchain Data Analysis",
        "home_intro": "Welcome to this interactive blockchain data visualization app. Use the menu on the left to navigate through the different sections.",
        "home_bitcoin_title": "Bitcoin Dashboard",
        "home_bitcoin_desc": "View real-time statistics of the Bitcoin blockchain (price, block count, pending transactions, etc.).",
        "home_solana_title": "Solana Dashboard",
        "home_solana_desc": "View Solana network performance (transactions per second, SOL price, latest blocks, etc.).",
        "home_comparison_title": "BTC vs SOL Comparison",
        "home_comparison_desc": "Compare Bitcoin and Solana trends (price, performance) with interactive charts.",
        "home_education_title": "Educational Page",
        "home_education_desc": "Learn the basics of blockchain, the history of Bitcoin, and the architecture of Solana.",
        "page_title_home": "Home | Blockchain Analysis",
        "page_title_bitcoin": "Bitcoin | Blockchain Analysis",
        "page_title_solana": "Solana | Blockchain Analysis",
        "page_title_comparison": "BTC vs SOL | Blockchain Analysis",
        "page_title_education": "Education | Blockchain Analysis",
        "bitcoin_title": "Bitcoin - Blockchain Statistics",
        "solana_title": "Solana - Network Statistics",
        "comparison_title": "Bitcoin vs Solana Comparison",
        "education_title": "Blockchain, Bitcoin & Solana - Explanation",
        "btc_price_label": "Bitcoin Price (USD)",
        "btc_block_label": "Latest Block",
        "btc_mempool_label": "Mempool Transactions",
        "sol_price_label": "Solana Price (USD)",
        "sol_block_label": "Latest Block",
        "sol_tps_label": "Transactions per Second (TPS)",
        "tps_chart_title": "Solana TPS (Last 60 min)",
        "mempool_chart_title": "Bitcoin Mempool Transactions (7 days)",
        "comp_chart_title": "Bitcoin vs Solana Price (USD, 30d)",
        "edu_blockchain_title": "What is Blockchain?",
        "edu_blockchain_text": """A **blockchain** is a distributed ledger technology that emerged with Bitcoin in 2009 (following the publication of Satoshi Nakamoto's whitepaper in 2008). It allows transactions to be stored transparently and securely in a chain of blocks: each block contains a cryptographic pointer to the previous block, making it nearly impossible to tamper with recorded data. The fundamental principles of a blockchain are **decentralization** (no central authority; the network is maintained by a peer-to-peer network of nodes), **immutability** (confirmed records cannot be altered), **transparency** (transactions are visible and verifiable by anyone), and a **consensus** mechanism that allows nodes to agree on the state of the ledger without prior trust. The first application of blockchain was the cryptocurrency Bitcoin, but the technology has since expanded to many domains beyond digital currency.""",
        "edu_bitcoin_title": "Bitcoin",
        "edu_bitcoin_text": """**Bitcoin** is the world's first cryptocurrency, described by Satoshi Nakamoto in a whitepaper in October 2008 and launched in January 2009. Over time, Bitcoin evolved from an experimental project used by a small group of enthusiasts (for example, the famous 10,000 BTC transaction for two pizzas in 2010) into a widely adopted digital asset with a market capitalization of hundreds of billions of dollars.

In terms of how it works, Bitcoin uses a **Proof of Work** consensus mechanism: participants called *miners* use computing power to solve a cryptographic puzzle (finding a block hash) in order to validate and add a new block of transactions to the chain, roughly every 10 minutes. The winning miner is rewarded with newly minted bitcoins (the block reward) as well as the transaction fees contained in the block. Bitcoin's supply is limited to 21 million coins, a cap enforced by the protocol and ensured by the periodic halving of the block reward (halvings occurring approximately every 4 years).

The Bitcoin network is decentralized, consisting of thousands of nodes worldwide that verify and propagate transactions. Pending transactions are collected in the **mempool** waiting to be included in a block. Bitcoin favors security and decentralization at the expense of speed: the network handles only about 7 transactions per second on average, which can lead to high fees and confirmation delays during times of high demand.""",
        "edu_solana_title": "Solana",
        "edu_solana_text": """**Solana** is a high-performance blockchain launched in 2020 by Anatoly Yakovenko. Its architecture relies on an innovative mechanism called **Proof of History** combined with **Proof of Stake** to achieve very fast consensus. Proof of History provides a cryptographic timestamp, creating a verifiable order of events, which helps dramatically increase transaction throughput.

Thanks to these innovations, Solana can theoretically process up to ~65,000 transactions per second, and its block time is around 400 milliseconds, making it much faster than Bitcoin. Unlike Bitcoin, Solana does not use Proof of Work mining: instead, network validators participate in consensus by *staking* SOL tokens (putting their funds at stake) and validating blocks. This removes the need for massive energy expenditure, making Solana more energy-efficient.

Solana also supports smart contracts and decentralized applications (features inspired by Ethereum) which are not native to Bitcoin. As a trade-off for its high performance, Solana is sometimes considered less decentralized than Bitcoin because it has fewer validators (partly due to the high hardware requirements to run a high-throughput node). Nevertheless, Solana aims to provide a scalable infrastructure for DeFi, NFTs, and other use cases that require very high transaction throughput."""
    },
    'RU': {
        "language_label": "Язык",
        "home_title": "Интерактивный анализ данных блокчейна",
        "home_intro": "Добро пожаловать в интерактивное приложение для визуализации данных блокчейна. Воспользуйтесь меню слева для перехода по различным разделам.",
        "home_bitcoin_title": "Дашборд Bitcoin",
        "home_bitcoin_desc": "Отображение в реальном времени статистики блокчейна Bitcoin (цена, количество блоков, транзакции в мемпуле и др.)",
        "home_solana_title": "Дашборд Solana",
        "home_solana_desc": "Показатели сети Solana (транзакции в секунду, цена SOL, последние блоки и др.)",
        "home_comparison_title": "Сравнение BTC vs SOL",
        "home_comparison_desc": "Сравните показатели Bitcoin и Solana (динамика цен, производительность) на интерактивных графиках.",
        "home_education_title": "Обучающая страница",
        "home_education_desc": "Узнайте основы технологии блокчейн, историю Bitcoin и устройство Solana.",
        "page_title_home": "Главная | Анализ блокчейна",
        "page_title_bitcoin": "Биткоин | Анализ блокчейна",
        "page_title_solana": "Солана | Анализ блокчейна",
        "page_title_comparison": "BTC vs SOL | Анализ блокчейна",
        "page_title_education": "Обучение | Анализ блокчейна",
        "bitcoin_title": "Биткоин - статистика блокчейна",
        "solana_title": "Солана - статистика сети",
        "comparison_title": "Сравнение Bitcoin vs Solana",
        "education_title": "Блокчейн, Bitcoin и Solana - объяснение",
        "btc_price_label": "Цена Биткоина (USD)",
        "btc_block_label": "Последний блок",
        "btc_mempool_label": "Транзакции в мемпуле",
        "sol_price_label": "Цена Соланы (USD)",
        "sol_block_label": "Последний блок",
        "sol_tps_label": "Транзакций в секунду (TPS)",
        "tps_chart_title": "TPS Solana (последние 60 мин)",
        "mempool_chart_title": "Транзакции в мемпуле Bitcoin (7 дней)",
        "comp_chart_title": "Цена Bitcoin vs Solana (USD, 30 дней)",
        "edu_blockchain_title": "Что такое блокчейн?",
        "edu_blockchain_text": """**Блокчейн** — это технология распределенного реестра, появившаяся вместе с Биткоином в 2009 году (после публикации концепции Сатоси Накамото в 2008 году). Блокчейн позволяет хранить транзакции прозрачно и безопасно в виде последовательной цепочки блоков: каждый блок содержит криптографическую ссылку (хеш) на предыдущий блок, что практически исключает подделку записей. Основные принципы блокчейна — это **децентрализация** (отсутствие центрального управляющего органа, сеть поддерживается множеством узлов), **неизменяемость** (записи, подтвержденные в цепи, не могут быть изменены задним числом), **прозрачность** (транзакции видимы и проверяемы всеми участниками) и механизм **консенсуса**, позволяющий узлам сети договориться об общем состоянии реестра без доверия друг к другу. Первым применением технологии блокчейн стала криптовалюта Bitcoin, однако сегодня блокчейны используются во многих сферах помимо цифровых валют.""",
        "edu_bitcoin_title": "Bitcoin",
        "edu_bitcoin_text": """**Bitcoin (Биткоин)** — первая в мире криптовалюта, описанная Сатоси Накамото в октябре 2008 года и запущенная в январе 2009 года. Исторически Биткоин прошел путь от эксперимента для узкого круга энтузиастов (например, знаменитая покупка двух пицц за 10 000 BTC в 2010 году) до широко распространенного цифрового актива с рыночной капитализацией в сотни миллиардов долларов.

С точки зрения работы системы, Bitcoin использует механизм консенсуса **Proof of Work (доказательство работы)**: участники сети, называемые *майнерами*, затрачивают вычислительные ресурсы для решения криптографической задачи (подбора хеша блока) с целью валидации и добавления нового блока транзакций в цепочку примерно каждые 10 минут. Победивший майнер получает вознаграждение в виде новых биткоинов (награда за блок), а также комиссии за транзакции, включенные в блок. Эмиссия биткоина ограничена 21 миллионом монет — этот предел запрограммирован в протоколе и поддерживается за счет периодического уменьшения награды (так называемый «халвинг» примерно каждые 4 года).

Bitcoin-сеть децентрализована: тысячи узлов по всему миру проверяют и передают транзакции. Неподтвержденные транзакции накапливаются в **мемпуле** (общем пуле) в ожидании включения в блок. Bitcoin делает упор на безопасность и децентрализацию в ущерб скорости: сеть обрабатывает лишь около 7 транзакций в секунду, что во время высокого спроса приводит к перегрузке мемпула, росту комиссий и увеличению времени подтверждения транзакций.""",
        "edu_solana_title": "Solana",
        "edu_solana_text": """**Solana (Солана)** — высокопроизводительный блокчейн, запущенный в 2020 году Анатолием Яковенко. В его архитектуре применяется инновационный механизм **Proof of History (доказательство истории)** в сочетании с **Proof of Stake (доказательство доли)** для достижения очень быстрого консенсуса. Proof of History предоставляет криптографическую отметку времени, формируя проверяемую хронологию событий, что помогает значительно увеличить пропускную способность транзакций.

Благодаря этому Solana теоретически способна обрабатывать до ~65 000 транзакций в секунду, а время блока составляет около 400 миллисекунд — значительно быстрее, чем у биткоина. В отличие от биткоина, Solana не использует майнинг на Proof of Work: согласие достигается валидаторами — узлами сети, которые *стейкают* (держат на кону) монеты SOL и подтверждают новые блоки. Это устраняет необходимость в энергозатратном вычислительном процессе и делает Solana более энергоэффективной.

Solana также поддерживает выполнение умных контрактов и децентрализованных приложений (как в Ethereum), чего нет в протоколе биткоина. Обратной стороной высокой производительности является потенциально более низкая децентрализация: число валидаторов Solana относительно невелико (частично из-за высоких технических требований для участия), поэтому сеть больше зависит от крупных узлов по сравнению с Bitcoin. Тем не менее, Solana стремится предоставить масштабируемую инфраструктуру для DeFi, NFT и других приложений, требующих очень высокой скорости обработки транзакций."""    
    }
}

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Фев 22 2023 г., 14:06
-- Версия сервера: 10.4.24-MariaDB
-- Версия PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `jktv22_school`
--

-- --------------------------------------------------------

--
-- Структура таблицы `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `title` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` text COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL COMMENT 'date publish'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `posts`
--

INSERT INTO `posts` (`id`, `title`, `description`, `image`, `date`) VALUES
(1, 'Релиз PHP 5.2.11!', 'Команда разработчиков PHP анонсировала о выпуске нового релиза: PHP 5.2.11 и рекомендует обновить версию.\r\n\r\nВ центре внимания нового релиза - улучшение стабильности ветки PHP 5.2.x.\r\nБолее 75 ошибок исправлено, некоторые связанные с безопасностью.\r\nРазработчикам и пользователям рекомендуется обновить версию PHP 5.2.x до 5.2.11.\r\nБолее подробную информацию о релизе PHP 5.2.11', 'https://uploads.hb.cldmail.ru/geekbrains/public/ckeditor_assets/pictures/4708/content-6d060b090a0c372d005a88b0155b2514.png', '2009-09-23'),
(2, 'Бот ChatGPT стал самым быстро растущим приложением в истории — уже более 100 миллионов пользователей', 'Еще в конце прошлого года стало ясно, что ChatGPT — ИИ-бот от OpenAI, поставит как минимум несколько рекордов по скорости роста. И не удивительно, даже если этот бот допускает некоторые ошибки, его можно применять везде....', 'https://cdn.shazoo.ru/c1200x525/671710_NyPY0pB_chatgpt.jpg', '2023-02-03'),
(3, 'Valve обновила античит Dota 2 и после этого навсегда заблокировала 40 тыс. пользователей', 'Valve сообщила, что обновила античит онлайн игры Dota 2 и разом заблокировала более 40 тыс. игроков. Вместе с этим студия поблагодарила пользователей, которые играют честно и помогают Valve бороться с нарушителями.', 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota2_social.jpg', '2023-02-22'),
(4, 'Россиянин успешно защитил диплом, написанный с помощью ChatGPT', 'ИИ и нейросети — будущее человечества, которое, похоже, уже наступило. В твиттере молодой человек под ником @biblikz написал тред, в котором рассказал, как ему удалось защитить диплом, написанный с помощью GhatGPT — текстовой нейросети компании...', 'https://cdn.shazoo.ru/c1200x525/671241_JNjVPU5_shazoo.jpg', '2023-02-01');

-- --------------------------------------------------------

--
-- Структура таблицы `speciality`
--

CREATE TABLE `speciality` (
  `id` int(11) NOT NULL,
  `nameSpec` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `duration` int(2) NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `speciality`
--

INSERT INTO `speciality` (`id`, `nameSpec`, `duration`, `image`, `description`) VALUES
(1, 'Повар', 3, '', ''),
(2, 'Инфотехнология', 2, '', ''),
(3, 'Слесарь', 1, '', '');

-- --------------------------------------------------------

--
-- Структура таблицы `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `firstName` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dataBirth` date NOT NULL,
  `gender` enum('m','n') COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `year` int(4) NOT NULL,
  `mobil` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `photo` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `specid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `student`
--

INSERT INTO `student` (`id`, `firstName`, `dataBirth`, `gender`, `address`, `year`, `mobil`, `photo`, `specid`) VALUES
(1, 'Медведев', '1993-02-03', 'm', 'Кохтла-Ярве', 2023, '88005553535', '2.jpg', 2),
(2, 'Сидоров', '2004-02-04', 'm', 'Йыхви', 2023, '8800553453', '1513.jpg', 1),
(3, 'Галкина', '2003-04-01', 'n', 'Тойла', 2023, '124224242', 'photo.jpg', 3),
(4, 'Пупкин', '2002-04-01', 'm', 'Таллинн', 2022, '8800553453', '', 3);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `role` enum('admin','moderator','user') COLLATE utf8_unicode_ci NOT NULL DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `username`, `role`) VALUES
(1, 'admin@test.ee ', '$2y$12$mjv/GPng4oQFohhkPl8RPucmgRDFVs/UCVP02US.r92ra09kK4d7u ', 'Admin', 'admin'),
(2, 'moderator@test.ee', '$2y$12$mjv/GPng4oQFohhkPl8RPucmgRDFVs/UCVP02US.r92ra09kK4d7u ', 'Moderator ', 'moderator'),
(3, 'user@test.ee', '$2y$12$mjv/GPng4oQFohhkPl8RPucmgRDFVs/UCVP02US.r92ra09kK4d7u', 'User', 'user');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `speciality`
--
ALTER TABLE `speciality`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD KEY `spaceid` (`specid`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `speciality`
--
ALTER TABLE `speciality`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`specid`) REFERENCES `speciality` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

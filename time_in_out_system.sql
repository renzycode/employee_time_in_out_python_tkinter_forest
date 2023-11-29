-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2023 at 12:42 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `time_in_out_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `e_id` mediumtext DEFAULT NULL,
  `name` mediumtext DEFAULT NULL,
  `password` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `e_id`, `name`, `password`) VALUES
(1, 'e-1111', 'Raulyo Renan', 'password'),
(2, 'e-2222', 'Salbutado Ryan', '1234'),
(3, 'e-3333', 'Himenez Bangaan', 'pass'),
(4, 'e-4444', 'Ryan Reynolds', '123');

-- --------------------------------------------------------

--
-- Table structure for table `time_in_out`
--

CREATE TABLE `time_in_out` (
  `id` int(11) NOT NULL,
  `e_id` mediumtext DEFAULT NULL,
  `name` mediumtext DEFAULT NULL,
  `time_in` mediumtext DEFAULT NULL,
  `time_out` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `time_in_out`
--

INSERT INTO `time_in_out` (`id`, `e_id`, `name`, `time_in`, `time_out`) VALUES
(5, 'e-1111', 'Raulyo Renan', '03:17 PM', '03:17 PM'),
(6, 'e-2222', 'Salbutado Ryan', '03:17 PM', '03:18 PM');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `time_in_out`
--
ALTER TABLE `time_in_out`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `time_in_out`
--
ALTER TABLE `time_in_out`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

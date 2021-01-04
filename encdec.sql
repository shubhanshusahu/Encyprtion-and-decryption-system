-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2021 at 10:54 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `encdec`
--

-- --------------------------------------------------------

--
-- Table structure for table `dectext`
--

CREATE TABLE `dectext` (
  `sno` int(3) NOT NULL,
  `text` text NOT NULL,
  `decrypted` text NOT NULL,
  `keyno` int(3) NOT NULL,
  `date` varchar(20) NOT NULL,
  `user` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dectext`
--

INSERT INTO `dectext` (`sno`, `text`, `decrypted`, `keyno`, `date`, `user`) VALUES
(7, 'qk3foyf?Dfeded', 'key is =6 /\\/\\', -6, '27-12-20 14:21:19', 'sss'),
(8, 'xlivi', 'there', -4, '28-12-20 08:56:10', 'there'),
(9, 'lippsBdXlmwdmwdWtigmepdw1qfspwd=%^&*()}:|', 'hellow This is Special symbols (!@#$%^,.)', -4, '28-12-20 15:51:49', 'sss'),
(10, 'xlmwdriihwdxsdfidirgv1txihd567769', 'this needs to be encrypted 123325', -4, '04-01-21 12:07:17', 'rishab'),
(11, 'nhCclvc6', 'key is 3', -3, '04-01-21 12:08:33', 'rishab');

-- --------------------------------------------------------

--
-- Table structure for table `enctext`
--

CREATE TABLE `enctext` (
  `sno` int(2) NOT NULL,
  `text` text NOT NULL,
  `encrypted` text NOT NULL,
  `keyno` int(3) DEFAULT NULL,
  `date` varchar(20) NOT NULL,
  `user` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `enctext`
--

INSERT INTO `enctext` (`sno`, `text`, `encrypted`, `keyno`, `date`, `user`) VALUES
(39, 'key is =6 /\\/\\', 'qk3foyf?Dfeded', 6, '27-12-20 14:20:53', 'sss'),
(40, 'this is !@#$%^&* symboles', 'znoyfoyf&*()_+=|fy3shurky', 6, '27-12-20 14:25:51', 'sss'),
(41, 'hello', 'nkrru', 6, '27-12-20 14:28:04', 'sss'),
(42, 'hello', 'jgnnq', 2, '27-12-20 14:28:29', 'sss'),
(43, 'there', 'xlivi', 4, '28-12-20 08:55:52', 'there'),
(44, 'abcd', 'defg', 3, '28-12-20 10:36:23', 'sss'),
(45, 'sdfs', 'whjw', 4, '28-12-20 11:00:34', 'sss'),
(46, 'hellow This is Special symbols (!@#$%^,.)', 'lippsBdXlmwdmwdWtigmepdw1qfspwd=%^&*()}:|', 4, '28-12-20 15:51:04', 'sss'),
(47, 'sdf', 'whj', 4, '28-12-20 15:52:19', 'sss'),
(48, 'this is encrypted using key=3', 'wklvclvchqfuCswhgcxvlqjcnhC>6', 3, '28-12-20 15:53:16', 'sss'),
(49, 'RIYA pagal hai itnee1234325@#$@', 'VM#Gdtekepdlemdmxrii5678769^&*^', 4, '28-12-20 15:56:25', 'shubhanshu'),
(50, 'sdfsaf', 'whjwej', 4, '28-12-20 16:41:45', 'amit'),
(51, 'this needs to be Encrypted', 'uijtaoffetaupacfaFodszqufe', 1, '28-12-20 16:53:10', 'shubhanshu'),
(52, 'this needs to be encrypted 123325', 'xlmwdriihwdxsdfidirgv1txihd567769', 4, '04-01-21 12:06:37', 'rishab'),
(53, 'key is 3', 'nhCclvc6', 3, '04-01-21 12:07:48', 'rishab');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `name` varchar(20) NOT NULL,
  `user` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`name`, `user`, `password`) VALUES
('', 'shiva', 'shiva123'),
('shubanshu', 'sss', '123'),
('shubhanshu sahu', 'ss', '123'),
('shubhanshu sahu', 'shubhanshu', '123'),
('shiva sahu', 'shiv', '1234'),
('shubhanshu sahu', 'shubh123', '123'),
('riya', 'riya', '111'),
('we', 'we', '123'),
('Arnav yadav', 'arnav', '123'),
('hello', 'there', 'abc'),
('shubhanshu sahu', 'shiba 1234', 'this'),
('Amitabh Bachhan', 'amit', 'ami123'),
('rishabh', 'rishab', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dectext`
--
ALTER TABLE `dectext`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `enctext`
--
ALTER TABLE `enctext`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dectext`
--
ALTER TABLE `dectext`
  MODIFY `sno` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `enctext`
--
ALTER TABLE `enctext`
  MODIFY `sno` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

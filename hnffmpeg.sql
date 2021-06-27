/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80018
Source Host           : localhost:3306
Source Database       : hnffmpeg

Target Server Type    : MYSQL
Target Server Version : 80018
File Encoding         : 65001

Date: 2021-06-27 17:16:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for hn_video
-- ----------------------------
DROP TABLE IF EXISTS `hn_video`;
CREATE TABLE `hn_video` (
  `md` varchar(255) COLLATE utf8_bin NOT NULL,
  `url` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  `path` varchar(255) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Table structure for user_log
-- ----------------------------
DROP TABLE IF EXISTS `user_log`;
CREATE TABLE `user_log` (
  `userId` bigint(255) NOT NULL,
  `opedate` datetime NOT NULL,
  `pushback` tinyint(2) NOT NULL,
  `url` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL COMMENT '用户日志',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

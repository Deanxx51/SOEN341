/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50517
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50517
File Encoding         : 65001

Date: 2014-01-11 23:10:18
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `pic`
-- ----------------------------
DROP TABLE IF EXISTS `pic`;
CREATE TABLE `pic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pic_name` varchar(60) NOT NULL,
  `pic_url` varchar(60) NOT NULL,
  `love` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pic
-- ----------------------------
INSERT INTO `pic` VALUES ('1', '1', 's1.jpg', '1');
INSERT INTO `pic` VALUES ('2', '2', 's2.jpg', '0');

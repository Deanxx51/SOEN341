/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50517
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50517
File Encoding         : 65001

Date: 2014-01-11 23:10:27
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `pic_ip`
-- ----------------------------
DROP TABLE IF EXISTS `pic_ip1`;
CREATE TABLE `pic_ip1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pic_id` int(11) NOT NULL,
  `ip` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pic_ip
-- ----------------------------
INSERT INTO `pic_ip1` VALUES ('1', '1', '127.0.0.1');

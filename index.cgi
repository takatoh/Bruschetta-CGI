#!/usr/bin/env ruby
# encoding: utf-8

require 'cgi'
require 'erb'
require 'httpclient'
require 'json'


@cgi = CGI.new
@client = HTTPClient.new


def main
  page = @cgi["page"].empty? ? 1 : @cgi["page"].to_i
  index(page)
end


def index(page)
  @title = "Bruschetta CGI"
  offset = 25 * (page - 1)
  json = @client.get("http://bruschetta/api/books/?limit=25&offset=#{offset.to_s}").body
  @books = JSON.parse(json)["books"]
  template = File.read("./views/index.erb")
  erb = ERB.new(template)

  print_header
  print erb.result
end


def print_header
  print "content-type: text/html\n\n"
end



main
